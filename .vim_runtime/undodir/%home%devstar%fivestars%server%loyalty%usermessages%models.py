Vim�UnDo� �"3U�ݚ�)�\m�yL��yr�2_O�    �   -        max_length=34, blank=True, null=True)   =                          P��    _�                     0       ����                                                                                                                                                                                                                                                                                                                                                             P��     �   .   0   �          user = models.ForeignKey(   >UserProfile, blank=True, null=True, on_delete=models.SET_NULL)�   /   1   �      F        UserProfile, blank=True, null=True, on_delete=models.SET_NULL)5�_�                    6       ����                                                                                                                                                                                                                                                                                                                                                             P��     �   4   6   �      '    phonefrom = models.BigIntegerField(   6help_text="Put the user's phone number in this field")�   5   7   �      >        help_text="Put the user's phone number in this field")5�_�                    7       ����                                                                                                                                                                                                                                                                                                                                                             P��     �   5   7   �      %    phoneto = models.BigIntegerField(   3help_text="IF EMPTY: Put 4083009228 in this field")�   6   8   �      ;        help_text="IF EMPTY: Put 4083009228 in this field")5�_�                    :       ����                                                                                                                                                                                                                                                                                                                                                             P��     �   8   :   �      %    cancel_reason = models.CharField(   6max_length=20, choices=CANCEL_REASON, default='Other')�   9   ;   �      >        max_length=20, choices=CANCEL_REASON, default='Other')5�_�                     =       ����                                                                                                                                                                                                                                                                                                                                                             P��    �   ;   =   �      +    received_twilio_sid = models.CharField(   %max_length=34, blank=True, null=True)�   <   >   �      -        max_length=34, blank=True, null=True)5��