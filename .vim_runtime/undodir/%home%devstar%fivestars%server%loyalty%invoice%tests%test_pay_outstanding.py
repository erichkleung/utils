Vim�UnDo� [���Gj�1�?������=-{�[p'��bE��   �   I            pd_to_amount_paid, excepted_result, "did not pay the statem")   ^                          P��    _�                     )       ����                                                                                                                                                                                                                                                                                                                                                             Pʂ+     �   '   )   �      %        payment_data.pay = MagicMock(   ?return_value=dict(is_success=True, transaction_id=uuid1().hex))�   (   *   �      K            return_value=dict(is_success=True, transaction_id=uuid1().hex))5�_�                    *       ����                                                                                                                                                                                                                                                                                                                                                             Pʂ/    �   (   *   �      9        b1_statements = BusinessStatement.objects.filter(   business__id=1).order_by('id')�   )   +   �      *            business__id=1).order_by('id')5�_�                    /       ����                                                                                                                                                                                                                                                                                                                )   8                                        PʂG     �   .   1   �      a        # second statement is not paid for, so with both statement should only charge statement 25�_�                    /        ����                                                                                                                                                                                                                                                                                                                0                                           PʂH    �   .   0                  5�_�                   G       ����                                                                                                                                                                                                                                                                                                                0                                           P��2     �   F   H   �      C            payer.pay_outstanding_by_payment_data(payment_data), 0,5�_�                    G       ����                                                                                                                                                                                                                                                                                                                0                                           P��3    �   E   G   �              self.assertEquals(   7payer.pay_outstanding_by_payment_data(payment_data), 0,�   F   H   �      C            payer.pay_outstanding_by_payment_data(payment_data), 0,5�_�      	              @       ����                                                                                                                                                                                                                                                                                                                F                                           P��O    �   >   @   �      1        amount_paid = PaymentTracker.objects.get(   "statement=b1_statements[2]).amount�   ?   A   �      .            statement=b1_statements[2]).amount5�_�      
           	   o       ����                                                                                                                                                                                                                                                                                                                ?   0                                        P��J     �   m   o   �      9        payer.email_invoice_paid.assert_called_once_with(   ${payer.payment_datas.all()[0]: 11.5}�   n   p   �      0            {payer.payment_datas.all()[0]: 11.5}5�_�   	              
   n   ]    ����                                                                                                                                                                                                                                                                                                                ?   0                                        P��N     �   m   o   �      ]        payer.email_invoice_paid.assert_called_once_with({payer.payment_datas.all()[0]: 11.5}   	        )�   m   o   �      ]        payer.email_invoice_paid.assert_called_once_with({payer.payment_datas.all()[0]: 11.5}5�_�   
                 w       ����                                                                                                                                                                                                                                                                                                                ?   0                                        P��[     �   u   w   �      7            result[pd] = BusinessStatement.objects.get(   &business__payment_data=pd).total / 100�   v   x   �      6                business__payment_data=pd).total / 1005�_�                    T       ����                                                                                                                                                                                                                                                                                                                ?   0                                        P��v     �   R   T   �                  pd.pay = MagicMock(   ?return_value=dict(is_success=True, transaction_id=uuid1().hex))�   S   U   �      O                return_value=dict(is_success=True, transaction_id=uuid1().hex))5�_�                     ^       ����                                                                                                                                                                                                                                                                                                                ?   0                                        P��    �   \   ^   �              self.assertEquals(   =pd_to_amount_paid, excepted_result, "did not pay the statem")�   ]   _   �      I            pd_to_amount_paid, excepted_result, "did not pay the statem")5�_�                    e       ����                                                                                                                                                                                                                                                                                                                0                                           PʂR     �   d   f   �      Tests pay_outstanding_method�   c   f   �      (        """ Tests pay_outstanding_method5��