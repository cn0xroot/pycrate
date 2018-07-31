# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.3
# *
# * Copyright 2018. Benoit Michau. ANSSI.
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
# * File Name : pycrate_csn1dir/packet_downlink_ack_nack_message_content.py
# * Created : 2018-07-30
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 11.2.6 Packet Downlink Ack/Nack
# top-level object: Packet Downlink Ack/Nack message content

# external references
from pycrate_csn1dir.ack_nack_description_ie import ack_nack_description_ie
from pycrate_csn1dir.channel_request_description_ie import channel_request_description_ie
from pycrate_csn1dir.iu_mode_channel_request_description_ie import iu_mode_channel_request_description_ie
from pycrate_csn1dir.padding_bits import padding_bits
from pycrate_csn1dir.iu_mode_channel_request_description_ie import extended_channel_request_description_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

channel_quality_report_struct = CSN1List(name='channel_quality_report_struct', list=[
  CSN1Bit(name='c_value', bit=6),
  CSN1Bit(name='rxqual', bit=3),
  CSN1Bit(name='sign_var', bit=6),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='i_level_tn0', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='i_level_tn1', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='i_level_tn2', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='i_level_tn3', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='i_level_tn4', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='i_level_tn5', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='i_level_tn6', bit=4)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='i_level_tn7', bit=4)])})])

packet_downlink_ack_nack_message_content = CSN1List(name='packet_downlink_ack_nack_message_content', list=[
  CSN1Bit(name='downlink_tfi', bit=5),
  CSN1Ref(name='ack_nack_description', obj=ack_nack_description_ie),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='channel_request_description', obj=channel_request_description_ie)])}),
  CSN1Ref(name='channel_quality_report', obj=channel_quality_report_struct),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Bit(bit=-1)]),
    '1': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='pfi', bit=7)])}),
    CSN1Alt(alt={
      '0': ('', [
      CSN1Bit(bit=-1)]),
      '1': ('', [
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Ref(name='iu_mode_channel_request_description', obj=iu_mode_channel_request_description_ie)])}),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='rb_id', bit=5)])}),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='timeslot_number', bit=3)])}),
      CSN1Alt(alt={
        '0': ('', [
        CSN1Bit(bit=-1)]),
        '1': ('', [
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Ref(name='extended_channel_request_description', obj=extended_channel_request_description_ie)])})]),
        None: ('', [])}),
      CSN1Alt(alt={
        '0': ('', [
        CSN1Bit(bit=-1)]),
        '1': ('', [
        CSN1Bit(name='early_tbf_establishment'),
        CSN1Ref(obj=padding_bits)]),
        None: ('', [])})]),
      None: ('', [])})]),
    None: ('', [])})])
