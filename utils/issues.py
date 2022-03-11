import starkbank
from datetime import datetime
import requests
from crendentials import credentials as cd
from utils import data as rd
import time


def schedule_issue():
    cd.credentials_init()
    x, z = 0, 0
    while True:
        time.sleep(2)
        while x < 12:
            time.sleep(2)
            issue_invoices()
            x = x + 1
        time.sleep(10800)


def issue_invoices():
    name = f'{rd.gen_random_name()}'
    value = f'{rd.gen_random_value()}'
    last_name = f'{rd.gen_random_lastname()}'

    invoices = starkbank.invoice.create([
        starkbank.Invoice(
            amount=int(f"{value}"),
            descriptions=[{'key': f'{name}', 'value': 'Not today'}],
            discounts=[{'percentage': 10, 'due': datetime(2022, 3, 12, 15, 23, 26, 689377)}],
            due=datetime(2022, 5, 12, 15, 23, 26, 689377),
            expiration=123456789,
            fine=2.5,
            interest=1.3,
            name=f"{name} {last_name}",
            tags=['New sword', 'Invoice #1234'],
            tax_id="29176331000169"
        )
    ])

    for invoice in invoices:
        try:
            requests.post(cd.webhook_url, data=dict(invoice))
        except:
            pass


def transfer_stark(amount_to_transfer):
    transfers = starkbank.transfer.create([
        starkbank.Transfer(
            amount=amount_to_transfer,
            tax_id="20.018.183/0001-80",
            name="Stark Bank S.A.",
            bank_code="20018183",
            branch_code="0001",
            account_type="payment",
            account_number="634132029348249",
            external_id="my-external-id",
            scheduled="2022-08-14",
            tags=["stark", "invoice/1234"]
        )
    ])

    for transfer in transfers:
        try:
            requests.post(cd.webhook_url, data=dict(transfer))
        except:
            pass
