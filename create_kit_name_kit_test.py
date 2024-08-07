# create_kit_name_kit_test.py
import pytest
from sender_stand_request import post_new_user, post_new_client_kit
from data import (
    KIT_BODY_MIN_CHAR,
    KIT_BODY_MAX_CHAR,
    KIT_BODY_EMPTY,
    KIT_BODY_TOO_LONG,
    KIT_BODY_SPECIAL_CHARS,
    KIT_BODY_SPACES,
    KIT_BODY_NUMBERS,
    KIT_BODY_MISSING_NAME,
    KIT_BODY_INVALID_TYPE
)

def get_new_user_token():
    return post_new_user()

def positive_assert(kit_body):
    auth_token = get_new_user_token()
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

def test_kit_name_min_char():
    positive_assert(KIT_BODY_MIN_CHAR)

def test_kit_name_max_char():
    positive_assert(KIT_BODY_MAX_CHAR)

def test_kit_name_empty():
    negative_assert_code_400(KIT_BODY_EMPTY)

def test_kit_name_too_long():
    negative_assert_code_400(KIT_BODY_TOO_LONG)

def test_kit_name_special_chars():
    positive_assert(KIT_BODY_SPECIAL_CHARS)

def test_kit_name_spaces():
    positive_assert(KIT_BODY_SPACES)

def test_kit_name_numbers():
    positive_assert(KIT_BODY_NUMBERS)

def test_kit_name_missing():
    negative_assert_code_400(KIT_BODY_MISSING_NAME)

def test_kit_name_invalid_type():
    negative_assert_code_400(KIT_BODY_INVALID_TYPE)
