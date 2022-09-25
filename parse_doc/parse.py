import gspread
from datetime import datetime
from django.conf import settings

from parse_doc.models import Orders
from parse_doc.exchange import get_rate_usd
#



class SyncBD():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, file, key) -> None:
        self.gp = gspread.service_account(filename=file)
        self.key = key

    def _read_sheets(self):
        sheet = self.gp.open_by_key(key=self.key).sheet1
        return sheet.get_all_values()[1:]

    def _get_orders_from_api(self):
        return {int(item[1]) for item in self.sheet_all}

    def _db_add(self, db_add_num):
        data_from_db = []
        for item in self.sheet_all:
            if int(item[1]) in db_add_num:
                data_from_db.append(Orders(number=item[1],
                                           price=item[2],
                                           delivery_time=datetime.strptime(item[3], '%d.%m.%Y')))

        Orders.objects.bulk_create(data_from_db)

    def _db_delete(self, db_delete_num):
        data_from_db = Orders.objects.filter(number__in=db_delete_num).delete()

    def sync(self):
        self.sheet_all = self._read_sheets()
        sheet_orders_num = self._get_orders_from_api()

        db_orders = Orders.objects.all()
        db_orders_num = {item.number for item in db_orders}

        rate = get_rate_usd()
        
        # синхронизируем по количеству записей. Удаляем, добавляем
        self._db_add(sheet_orders_num - db_orders_num)
        self._db_delete(db_orders_num-sheet_orders_num)

        # синхронизируем данные
        for item in self.sheet_all:
            Orders.objects.filter(number=int(item[1])).update(number=item[1],
                                                              price=item[2],
                                                              price_rub=float(item[2])*rate,
                                                              delivery_time=datetime.strptime(item[3], '%d.%m.%Y'))


sync_db = SyncBD(settings.GOOGLE_API_SETTINGS, settings.KEY)
get_rate_usd()