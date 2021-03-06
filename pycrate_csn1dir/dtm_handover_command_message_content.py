# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.4
# *
# * Copyright 2018. Benoit Michau. ANSSI. P1sec.
# *
# * This library is free software; you can redistribute it and/or
# * modify it under the terms of the GNU Lesser General Public
# * License as published by the Free Software Foundation; either
# * version 2.1 of the License, or (at your option) any later version.
# *
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# * Lesser General Public License for more details.
# *
# * You should have received a copy of the GNU Lesser General Public
# * License along with this library; if not, write to the Free Software
# * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 
# * MA 02110-1301  USA
# *
# *--------------------------------------------------------
# * File Name : pycrate_csn1dir/dtm_handover_command_message_content.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 11.2.46 DTM Handover Command
# top-level object: DTM Handover Command message content

# external references
from pycrate_csn1dir.padding_bits import padding_bits
from pycrate_csn1dir.cs_handover_radio_resources_ie import cs_handover_radio_resources_ie
from pycrate_csn1dir.rrc_container_ie import rrc_container_ie
from pycrate_csn1dir.nas_container_for_ps_handover_ie import nas_container_for_ps_handover_ie
from pycrate_csn1dir.dtm_handover_ps_radio_resources_3_ie import dtm_handover_ps_radio_resources_3_ie
from pycrate_csn1dir.global_tfi_ie import global_tfi_ie
from pycrate_csn1dir.dtm_handover_ps_radio_resources_2_ie import dtm_handover_ps_radio_resources_2_ie
from pycrate_csn1dir.dtm_handover_ps_radio_resources_ie import dtm_handover_ps_radio_resources_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

dtm_handover_to_a_gb_mode_payload_description_struct = CSN1List(name='dtm_handover_to_a_gb_mode_payload_description_struct', list=[
  CSN1Ref(name='dtm_handover_cs_rr_info', obj=cs_handover_radio_resources_ie),
  CSN1Alt(alt={
    '00': ('', [
    CSN1Ref(name='dtm_handover_ps_rr_info', obj=dtm_handover_ps_radio_resources_ie)]),
    '01': ('', [
    CSN1Ref(name='dtm_handover_ps_rr_2_info', obj=dtm_handover_ps_radio_resources_2_ie)]),
    '10': ('', [
    CSN1Ref(name='dtm_handover_ps_rr_3_info', obj=dtm_handover_ps_radio_resources_3_ie)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(obj=nas_container_for_ps_handover_ie)])})])

dtm_handover_command_message_content = CSN1List(name='dtm_handover_command_message_content', list=[
  CSN1Bit(name='page_mode', bit=2),
  CSN1List(list=[
    CSN1Val(name='', val='0'),
    CSN1Ref(name='global_tfi', obj=global_tfi_ie),
    CSN1List(list=[
      CSN1Alt(alt={
        '00': ('', [
        CSN1Ref(name='dtm_handover_to_a_gb_mode_payload', obj=dtm_handover_to_a_gb_mode_payload_description_struct)]),
        '01': ('', [
        CSN1Ref(name='dtm_handover_to_utran_payload', obj=rrc_container_ie)])}),
      CSN1Ref(obj=padding_bits)])])])

