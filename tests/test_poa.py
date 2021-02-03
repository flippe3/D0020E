import pytest, os, sys
import OauthDev.Token as Token
import OauthDev.Util as Util
import development.Constants as const

poa = Token.Poa(const.agent_mac_address, const.agent_name, const.agent_public_key,
            const.principal_name, const.principal_public_key,
            const.valid_period, const.id, const.message)

def test_valid_time():
    assert Token.validatePoaPeriod(poa.payload, "2021-02-02 18:00:00")

