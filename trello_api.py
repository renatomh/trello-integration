# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:15:00 2023

@author: RenatoHenz

Script with functions to communicate with Trello's API
"""

# Getting config data
from config import TRELLO_API_KEY, TRELLO_TOKEN

# Dependencies
import requests, json

# Function to get the user data
def get_me():
    # Defining API URL
    url = f"https://api.trello.com/1/members/me"

    # Defining query params
    query = {
        'key': TRELLO_API_KEY,
        'token': TRELLO_TOKEN,
    }

    # Making the API call
    response = requests.request("GET", url, params=query)

    # If request was successful, we'll return the data
    if response.ok: return json.loads(response.text)
    # Otherwise, we return an empty dict
    else: return {}

# Function to get the available boards for a specific user (member)
def get_boards(member_id):
    # Defining API URL
    url = f"https://api.trello.com/1/members/{member_id}/boards"

    # Defining query params
    query = {
        'key': TRELLO_API_KEY,
        'token': TRELLO_TOKEN,
    }

    # Making the API call
    response = requests.request("GET", url, params=query)

    # If request was successful, we'll return the data
    if response.ok: return json.loads(response.text)
    # Otherwise, we return an empty list
    else: return []

# Function to get the available lists for a specific board
def get_board_lists(board_id):
    # Defining API URL
    url = f"https://api.trello.com/1/boards/{board_id}/lists"

    # Defining query params
    query = {
        'key': TRELLO_API_KEY,
        'token': TRELLO_TOKEN,
    }

    # Making the API call
    response = requests.request("GET", url, params=query)

    # If request was successful, we'll return the data
    if response.ok: return json.loads(response.text)
    # Otherwise, we return an empty list
    else: return []

# Function to get the available labels for a specific board
def get_board_labels(board_id):
    # Defining API URL
    url = f"https://api.trello.com/1/boards/{board_id}/labels"

    # Defining query params
    query = {
        'key': TRELLO_API_KEY,
        'token': TRELLO_TOKEN,
    }

    # Making the API call
    response = requests.request("GET", url, params=query)

    # If request was successful, we'll return the data
    if response.ok: return json.loads(response.text)
    # Otherwise, we return an empty list
    else: return []

# Function to post a new card to a specific list from a board
def post_card(list_id, name, desc=None, labels_ids=[]):
    # Defining API URL
    url = "https://api.trello.com/1/cards"

    # Defining headers and query params
    headers = {
        'Accept': 'application/json'
    }
    query = {
        'key': TRELLO_API_KEY,
        'token': TRELLO_TOKEN,
        'idList': list_id,
        'name': name,
        'desc': desc,
        'idLabels': labels_ids,
    }

    # Making the API call
    response = requests.request("POST", url, headers=headers, params=query)

    # If request was successful, we'll return the data
    if response.ok: return json.loads(response.text)
    # Otherwise, we return None
    else: return None

# Function to post a new comment to a specific card
def post_card_comment(card_id, text):
    # Defining API URL
    url = f"https://api.trello.com/1/cards/{card_id}/actions/comments"

    # Defining headers and query params
    headers = {
        'Accept': 'application/json'
    }
    query = {
        'key': TRELLO_API_KEY,
        'token': TRELLO_TOKEN,
        'text': text,
    }

    # Making the API call
    response = requests.request("POST", url, headers=headers, params=query)

    # If request was successful, we'll return the data
    if response.ok: return json.loads(response.text)
    # Otherwise, we return None
    else: return None
