# -*- coding: utf-8 -*-
"""DNACenterAPI wireless API fixtures and tests.

Copyright (c) 2019-2021 Cisco Systems.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import pytest
from fastjsonschema.exceptions import JsonSchemaException
from dnacentersdk.exceptions import MalformedRequest
from tests.environment import DNA_CENTER_VERSION

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.2.2.3', reason='version does not match')


def is_valid_sensor_test_results(json_schema_validate, obj):
    json_schema_validate('jsd_dde2b077d6d052dcae5a76f4aac09c1d_v2_2_2_3').validate(obj)
    return True


def sensor_test_results(api):
    endpoint_result = api.wireless.sensor_test_results(
        end_time=0,
        site_id='string',
        start_time=0,
        test_failure_by='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_sensor_test_results(api, validator):
    try:
        assert is_valid_sensor_test_results(
            validator,
            sensor_test_results(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def sensor_test_results_default(api):
    endpoint_result = api.wireless.sensor_test_results(
        end_time=None,
        site_id=None,
        start_time=None,
        test_failure_by=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_sensor_test_results_default(api, validator):
    try:
        assert is_valid_sensor_test_results(
            validator,
            sensor_test_results_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_and_provision_ssid(json_schema_validate, obj):
    json_schema_validate('jsd_d825ae9a117f5b6bb65b7d78fd42513c_v2_2_2_3').validate(obj)
    return True


def create_and_provision_ssid(api):
    endpoint_result = api.wireless.create_and_provision_ssid(
        active_validation=True,
        enableFabric=True,
        flexConnect={'enableFlexConnect': True, 'localToVlan': 0},
        managedAPLocations=['string'],
        payload=None,
        ssidDetails={'name': 'string', 'securityLevel': 'string', 'enableFastLane': True, 'passphrase': 'string', 'trafficType': 'string', 'enableBroadcastSSID': True, 'radioPolicy': 'string', 'enableMACFiltering': True, 'fastTransition': 'string', 'webAuthURL': 'string'},
        ssidType='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_and_provision_ssid(api, validator):
    try:
        assert is_valid_create_and_provision_ssid(
            validator,
            create_and_provision_ssid(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_and_provision_ssid_default(api):
    endpoint_result = api.wireless.create_and_provision_ssid(
        active_validation=True,
        enableFabric=None,
        flexConnect=None,
        managedAPLocations=None,
        payload=None,
        ssidDetails=None,
        ssidType=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_and_provision_ssid_default(api, validator):
    try:
        assert is_valid_create_and_provision_ssid(
            validator,
            create_and_provision_ssid_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_ssid_and_provision_it_to_devices(json_schema_validate, obj):
    json_schema_validate('jsd_8e56eb2c294159d891b7dbe493ddc434_v2_2_2_3').validate(obj)
    return True


def delete_ssid_and_provision_it_to_devices(api):
    endpoint_result = api.wireless.delete_ssid_and_provision_it_to_devices(
        managed_aplocations='string',
        ssid_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_ssid_and_provision_it_to_devices(api, validator):
    try:
        assert is_valid_delete_ssid_and_provision_it_to_devices(
            validator,
            delete_ssid_and_provision_it_to_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_ssid_and_provision_it_to_devices_default(api):
    endpoint_result = api.wireless.delete_ssid_and_provision_it_to_devices(
        managed_aplocations='string',
        ssid_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_ssid_and_provision_it_to_devices_default(api, validator):
    try:
        assert is_valid_delete_ssid_and_provision_it_to_devices(
            validator,
            delete_ssid_and_provision_it_to_devices_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_enterprise_ssid(json_schema_validate, obj):
    json_schema_validate('jsd_fb757e8fce4b51ffa0ba1a8e5ae4d8c0_v2_2_2_3').validate(obj)
    return True


def get_enterprise_ssid(api):
    endpoint_result = api.wireless.get_enterprise_ssid(
        ssid_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_enterprise_ssid(api, validator):
    try:
        assert is_valid_get_enterprise_ssid(
            validator,
            get_enterprise_ssid(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_enterprise_ssid_default(api):
    endpoint_result = api.wireless.get_enterprise_ssid(
        ssid_name=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_enterprise_ssid_default(api, validator):
    try:
        assert is_valid_get_enterprise_ssid(
            validator,
            get_enterprise_ssid_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_enterprise_ssid(json_schema_validate, obj):
    json_schema_validate('jsd_bc33daf690ec5399a507829abfc4fe64_v2_2_2_3').validate(obj)
    return True


def create_enterprise_ssid(api):
    endpoint_result = api.wireless.create_enterprise_ssid(
        active_validation=True,
        basicServiceSetClientIdleTimeout=0,
        clientExclusionTimeout=0,
        enableBasicServiceSetMaxIdle=True,
        enableBroadcastSSID=True,
        enableClientExclusion=True,
        enableDirectedMulticastService=True,
        enableFastLane=True,
        enableMACFiltering=True,
        enableNeighborList=True,
        enableSessionTimeOut=True,
        fastTransition='string',
        mfpClientProtection='string',
        name='string',
        passphrase='string',
        payload=None,
        radioPolicy='string',
        securityLevel='string',
        sessionTimeOut=0,
        trafficType='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_enterprise_ssid(api, validator):
    try:
        assert is_valid_create_enterprise_ssid(
            validator,
            create_enterprise_ssid(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_enterprise_ssid_default(api):
    endpoint_result = api.wireless.create_enterprise_ssid(
        active_validation=True,
        basicServiceSetClientIdleTimeout=None,
        clientExclusionTimeout=None,
        enableBasicServiceSetMaxIdle=None,
        enableBroadcastSSID=None,
        enableClientExclusion=None,
        enableDirectedMulticastService=None,
        enableFastLane=None,
        enableMACFiltering=None,
        enableNeighborList=None,
        enableSessionTimeOut=None,
        fastTransition=None,
        mfpClientProtection=None,
        name=None,
        passphrase=None,
        payload=None,
        radioPolicy=None,
        securityLevel=None,
        sessionTimeOut=None,
        trafficType=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_enterprise_ssid_default(api, validator):
    try:
        assert is_valid_create_enterprise_ssid(
            validator,
            create_enterprise_ssid_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_enterprise_ssid(json_schema_validate, obj):
    json_schema_validate('jsd_25479623a94058a99acaaf8eb73c9227_v2_2_2_3').validate(obj)
    return True


def update_enterprise_ssid(api):
    endpoint_result = api.wireless.update_enterprise_ssid(
        active_validation=True,
        basicServiceSetClientIdleTimeout=0,
        clientExclusionTimeout=0,
        enableBasicServiceSetMaxIdle=True,
        enableBroadcastSSID=True,
        enableClientExclusion=True,
        enableDirectedMulticastService=True,
        enableFastLane=True,
        enableMACFiltering=True,
        enableNeighborList=True,
        enableSessionTimeOut=True,
        fastTransition='string',
        mfpClientProtection='string',
        name='string',
        passphrase='string',
        payload=None,
        radioPolicy='string',
        securityLevel='string',
        sessionTimeOut=0,
        trafficType='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_enterprise_ssid(api, validator):
    try:
        assert is_valid_update_enterprise_ssid(
            validator,
            update_enterprise_ssid(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_enterprise_ssid_default(api):
    endpoint_result = api.wireless.update_enterprise_ssid(
        active_validation=True,
        basicServiceSetClientIdleTimeout=None,
        clientExclusionTimeout=None,
        enableBasicServiceSetMaxIdle=None,
        enableBroadcastSSID=None,
        enableClientExclusion=None,
        enableDirectedMulticastService=None,
        enableFastLane=None,
        enableMACFiltering=None,
        enableNeighborList=None,
        enableSessionTimeOut=None,
        fastTransition=None,
        mfpClientProtection=None,
        name=None,
        passphrase=None,
        payload=None,
        radioPolicy=None,
        securityLevel=None,
        sessionTimeOut=None,
        trafficType=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_enterprise_ssid_default(api, validator):
    try:
        assert is_valid_update_enterprise_ssid(
            validator,
            update_enterprise_ssid_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_enterprise_ssid(json_schema_validate, obj):
    json_schema_validate('jsd_6a43afa4d91a5043996c682a7a7a2d62_v2_2_2_3').validate(obj)
    return True


def delete_enterprise_ssid(api):
    endpoint_result = api.wireless.delete_enterprise_ssid(
        ssid_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_enterprise_ssid(api, validator):
    try:
        assert is_valid_delete_enterprise_ssid(
            validator,
            delete_enterprise_ssid(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_enterprise_ssid_default(api):
    endpoint_result = api.wireless.delete_enterprise_ssid(
        ssid_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_enterprise_ssid_default(api, validator):
    try:
        assert is_valid_delete_enterprise_ssid(
            validator,
            delete_enterprise_ssid_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_wireless_profile(json_schema_validate, obj):
    json_schema_validate('jsd_9610a850fb6c5451a7ad20ba76f4ff43_v2_2_2_3').validate(obj)
    return True


def delete_wireless_profile(api):
    endpoint_result = api.wireless.delete_wireless_profile(
        wireless_profile_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_wireless_profile(api, validator):
    try:
        assert is_valid_delete_wireless_profile(
            validator,
            delete_wireless_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_wireless_profile_default(api):
    endpoint_result = api.wireless.delete_wireless_profile(
        wireless_profile_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_wireless_profile_default(api, validator):
    try:
        assert is_valid_delete_wireless_profile(
            validator,
            delete_wireless_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_ap_provision(json_schema_validate, obj):
    json_schema_validate('jsd_09f790a930d452708353c374f5c0f90f_v2_2_2_3').validate(obj)
    return True


def ap_provision(api):
    endpoint_result = api.wireless.ap_provision(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_ap_provision(api, validator):
    try:
        assert is_valid_ap_provision(
            validator,
            ap_provision(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def ap_provision_default(api):
    endpoint_result = api.wireless.ap_provision(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_ap_provision_default(api, validator):
    try:
        assert is_valid_ap_provision(
            validator,
            ap_provision_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_update_dynamic_interface(json_schema_validate, obj):
    json_schema_validate('jsd_36c00df3623b5a74ad41e75487ed9b77_v2_2_2_3').validate(obj)
    return True


def create_update_dynamic_interface(api):
    endpoint_result = api.wireless.create_update_dynamic_interface(
        active_validation=True,
        interfaceName='string',
        payload=None,
        vlanId=0
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_update_dynamic_interface(api, validator):
    try:
        assert is_valid_create_update_dynamic_interface(
            validator,
            create_update_dynamic_interface(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_update_dynamic_interface_default(api):
    endpoint_result = api.wireless.create_update_dynamic_interface(
        active_validation=True,
        interfaceName=None,
        payload=None,
        vlanId=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_update_dynamic_interface_default(api, validator):
    try:
        assert is_valid_create_update_dynamic_interface(
            validator,
            create_update_dynamic_interface_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_dynamic_interface(json_schema_validate, obj):
    json_schema_validate('jsd_2583c9fb8b0f5c69ba22f920e4044538_v2_2_2_3').validate(obj)
    return True


def get_dynamic_interface(api):
    endpoint_result = api.wireless.get_dynamic_interface(
        interface_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_dynamic_interface(api, validator):
    try:
        assert is_valid_get_dynamic_interface(
            validator,
            get_dynamic_interface(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_dynamic_interface_default(api):
    endpoint_result = api.wireless.get_dynamic_interface(
        interface_name=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_dynamic_interface_default(api, validator):
    try:
        assert is_valid_get_dynamic_interface(
            validator,
            get_dynamic_interface_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_dynamic_interface(json_schema_validate, obj):
    json_schema_validate('jsd_82bfd78707835bc8934cf0df1b0169fc_v2_2_2_3').validate(obj)
    return True


def delete_dynamic_interface(api):
    endpoint_result = api.wireless.delete_dynamic_interface(
        interface_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_dynamic_interface(api, validator):
    try:
        assert is_valid_delete_dynamic_interface(
            validator,
            delete_dynamic_interface(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_dynamic_interface_default(api):
    endpoint_result = api.wireless.delete_dynamic_interface(
        interface_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_dynamic_interface_default(api, validator):
    try:
        assert is_valid_delete_dynamic_interface(
            validator,
            delete_dynamic_interface_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_wireless_profile(json_schema_validate, obj):
    json_schema_validate('jsd_5135bbf7ce025bc2a291b90c37a6b898_v2_2_2_3').validate(obj)
    return True


def update_wireless_profile(api):
    endpoint_result = api.wireless.update_wireless_profile(
        active_validation=True,
        payload=None,
        profileDetails={'name': 'string', 'sites': ['string'], 'ssidDetails': [{'name': 'string', 'type': 'string', 'enableFabric': True, 'flexConnect': {'enableFlexConnect': True, 'localToVlan': 0}, 'interfaceName': 'string'}]}
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_wireless_profile(api, validator):
    try:
        assert is_valid_update_wireless_profile(
            validator,
            update_wireless_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_wireless_profile_default(api):
    endpoint_result = api.wireless.update_wireless_profile(
        active_validation=True,
        payload=None,
        profileDetails=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_update_wireless_profile_default(api, validator):
    try:
        assert is_valid_update_wireless_profile(
            validator,
            update_wireless_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_wireless_profile(json_schema_validate, obj):
    json_schema_validate('jsd_b95201b6a6905a10b463e036bf591166_v2_2_2_3').validate(obj)
    return True


def create_wireless_profile(api):
    endpoint_result = api.wireless.create_wireless_profile(
        active_validation=True,
        payload=None,
        profileDetails={'name': 'string', 'sites': ['string'], 'ssidDetails': [{'name': 'string', 'type': 'string', 'enableFabric': True, 'flexConnect': {'enableFlexConnect': True, 'localToVlan': 0}, 'interfaceName': 'string'}]}
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_wireless_profile(api, validator):
    try:
        assert is_valid_create_wireless_profile(
            validator,
            create_wireless_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_wireless_profile_default(api):
    endpoint_result = api.wireless.create_wireless_profile(
        active_validation=True,
        payload=None,
        profileDetails=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_wireless_profile_default(api, validator):
    try:
        assert is_valid_create_wireless_profile(
            validator,
            create_wireless_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_wireless_profile(json_schema_validate, obj):
    json_schema_validate('jsd_bbc1866a50505c0695ae243718d51936_v2_2_2_3').validate(obj)
    return True


def get_wireless_profile(api):
    endpoint_result = api.wireless.get_wireless_profile(
        profile_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_wireless_profile(api, validator):
    try:
        assert is_valid_get_wireless_profile(
            validator,
            get_wireless_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_wireless_profile_default(api):
    endpoint_result = api.wireless.get_wireless_profile(
        profile_name=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_get_wireless_profile_default(api, validator):
    try:
        assert is_valid_get_wireless_profile(
            validator,
            get_wireless_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_provision_update(json_schema_validate, obj):
    json_schema_validate('jsd_d0aab00569b258b481afedc35e6db392_v2_2_2_3').validate(obj)
    return True


def provision_update(api):
    endpoint_result = api.wireless.provision_update(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_provision_update(api, validator):
    try:
        assert is_valid_provision_update(
            validator,
            provision_update(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def provision_update_default(api):
    endpoint_result = api.wireless.provision_update(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_provision_update_default(api, validator):
    try:
        assert is_valid_provision_update(
            validator,
            provision_update_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_provision(json_schema_validate, obj):
    json_schema_validate('jsd_359718e31c795964b3bdf85da1b5a2a5_v2_2_2_3').validate(obj)
    return True


def provision(api):
    endpoint_result = api.wireless.provision(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_provision(api, validator):
    try:
        assert is_valid_provision(
            validator,
            provision(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def provision_default(api):
    endpoint_result = api.wireless.provision(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_provision_default(api, validator):
    try:
        assert is_valid_provision(
            validator,
            provision_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_psk_override(json_schema_validate, obj):
    json_schema_validate('jsd_f99c96c3a9b45ddaabc2c75ff8efa67f_v2_2_2_3').validate(obj)
    return True


def psk_override(api):
    endpoint_result = api.wireless.psk_override(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_psk_override(api, validator):
    try:
        assert is_valid_psk_override(
            validator,
            psk_override(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def psk_override_default(api):
    endpoint_result = api.wireless.psk_override(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_psk_override_default(api, validator):
    try:
        assert is_valid_psk_override(
            validator,
            psk_override_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_rf_profiles(json_schema_validate, obj):
    json_schema_validate('jsd_ac37d6798c0b593088952123df03bb1b_v2_2_2_3').validate(obj)
    return True


def retrieve_rf_profiles(api):
    endpoint_result = api.wireless.retrieve_rf_profiles(
        rf_profile_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_retrieve_rf_profiles(api, validator):
    try:
        assert is_valid_retrieve_rf_profiles(
            validator,
            retrieve_rf_profiles(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_rf_profiles_default(api):
    endpoint_result = api.wireless.retrieve_rf_profiles(
        rf_profile_name=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_retrieve_rf_profiles_default(api, validator):
    try:
        assert is_valid_retrieve_rf_profiles(
            validator,
            retrieve_rf_profiles_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_or_update_rf_profile(json_schema_validate, obj):
    json_schema_validate('jsd_5f24f6c07641580ba6ed710e92c2da16_v2_2_2_3').validate(obj)
    return True


def create_or_update_rf_profile(api):
    endpoint_result = api.wireless.create_or_update_rf_profile(
        active_validation=True,
        channelWidth='string',
        defaultRfProfile=True,
        enableBrownField=True,
        enableCustom=True,
        enableRadioTypeA=True,
        enableRadioTypeB=True,
        name='string',
        payload=None,
        radioTypeAProperties={'parentProfile': 'string', 'radioChannels': 'string', 'dataRates': 'string', 'mandatoryDataRates': 'string', 'powerThresholdV1': 0, 'rxSopThreshold': 'string', 'minPowerLevel': 0, 'maxPowerLevel': 0},
        radioTypeBProperties={'parentProfile': 'string', 'radioChannels': 'string', 'dataRates': 'string', 'mandatoryDataRates': 'string', 'powerThresholdV1': 0, 'rxSopThreshold': 'string', 'minPowerLevel': 0, 'maxPowerLevel': 0}
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_or_update_rf_profile(api, validator):
    try:
        assert is_valid_create_or_update_rf_profile(
            validator,
            create_or_update_rf_profile(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_or_update_rf_profile_default(api):
    endpoint_result = api.wireless.create_or_update_rf_profile(
        active_validation=True,
        channelWidth=None,
        defaultRfProfile=None,
        enableBrownField=None,
        enableCustom=None,
        enableRadioTypeA=None,
        enableRadioTypeB=None,
        name=None,
        payload=None,
        radioTypeAProperties=None,
        radioTypeBProperties=None
    )
    return endpoint_result


@pytest.mark.wireless
def test_create_or_update_rf_profile_default(api, validator):
    try:
        assert is_valid_create_or_update_rf_profile(
            validator,
            create_or_update_rf_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_rf_profiles(json_schema_validate, obj):
    json_schema_validate('jsd_97f3790386da5cd49480cb0503e59047_v2_2_2_3').validate(obj)
    return True


def delete_rf_profiles(api):
    endpoint_result = api.wireless.delete_rf_profiles(
        rf_profile_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_rf_profiles(api, validator):
    try:
        assert is_valid_delete_rf_profiles(
            validator,
            delete_rf_profiles(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_rf_profiles_default(api):
    endpoint_result = api.wireless.delete_rf_profiles(
        rf_profile_name='string'
    )
    return endpoint_result


@pytest.mark.wireless
def test_delete_rf_profiles_default(api, validator):
    try:
        assert is_valid_delete_rf_profiles(
            validator,
            delete_rf_profiles_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
