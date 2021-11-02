from brownie import accounts, config, SimpleStorage
import os

def test_deploy():
    #Arrange
    account = accounts[0]
    #Act
    simple_storage = SimpleStorage.deploy({"from":account})
    starting_value = simple_storage.retrieve()
    expected = 0
    #Assert
    assert starting_value == expected

def test_updating_storage():
    #Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from":account})
    #Act
    expected = 15
    simple_storage.store(expected,{"from":account})
    #Assert
    assert expected == simple_storage.retrieve()

    # account = accounts.add(config["wallets"]["from_key"])
    # simple_storage = SimpleStorage.deploy({"from":account})
    # stored_value = simple_storage.retrieve()
    # print(stored_value)
    # txn = simple_storage.store(15,{"from":account})
    # txn.wait(1)
    # updated_stored_value = simple_storage.retrieve()
    # print(updated_stored_value)