# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from unittest import mock

from django.db import DEFAULT_DB_ALIAS

from django.http import HttpRequest


class BillingViewTestCase():
    @mock.patch('connection')
    def test_billing_listing(self, mock_connections):
        mock_cursor = mock_connections.__getitem__(DEFAULT_DB_ALIAS).cursor.return_value.__enter__.return_value
        request = HttpRequest()
        request.context(type: 'billing')
        billingdata = billinglisting(request)

        # Demonstrating assert_* options:
        mock_cursor.execute.assert_called_once()
        mock_cursor.execute.assert_called()
        asserEqual('billing-view.html', billingdata.getView())
        
    @mock.patch('connection')
    def test_billing_object(self, mock_connections):
        mock_cursor = mock_connections.__getitem__(DEFAULT_DB_ALIAS).cursor.return_value.__enter__.return_value
        billing = Billing('b01', '09/09/2019', 'book_1', 'food', 'Food bill')
        mock.dictfetchall(return = billing)
        request = HttpRequest()
        request.context(type: 'billing')
        billingdata = getData('b01')

        # Demonstrating assert_* options:
        mock_cursor.execute.assert_called_once()
        mock_cursor.execute.assert_called()
        asserEqual(billing, billingdata.getData())
        
    @mock.patch('connection')
    def test_billing_update(self, mock_connections):
        mock_cursor = mock_connections.__getitem__(DEFAULT_DB_ALIAS).cursor.return_value.__enter__.return_value
        billing = Billing('b01', '09/09/2019', 'book_1', 'food', 'Food bill')
        context = {
        "fn": "update",
        "bookinglist": getDropDown('booking', 'booking_id'),
        "billingDetails": billing,
        "heading": 'Billing Update',
        }
        billing = Billing('b01', '09/09/2019', 'book_1', 'food', 'Food bill')
        mock.dictfetchall(return = billing)
        request = HttpRequest()
        request.context(type: 'billing')
        billingdata = update(request,'b01')

        # Demonstrating assert_* options:
        mock_cursor.execute.assert_called_once()
        mock_cursor.execute.assert_called()
        asserEqual(billing, billingdata.getData())
        asserEqual('billing-view.html', billingdata.getView())
        
    
        
    