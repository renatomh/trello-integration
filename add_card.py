# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:15:00 2023

@author: RenatoHenz

Script to create add cards to Trello's boards
"""

# Importing utilities functions
from trello_api import get_me, get_boards, get_board_labels, \
    get_board_lists, post_card, post_card_comment

# Selected board and list
selected_board = None
selected_list = None
# Selected labels for the card
selected_label_ids = []

# Function to show available boards
def show_boards():
    for idx, bd in enumerate(available_boards):
        print(f"{idx+1}: {bd['name']}")

# Function to show available lists
def show_lists():
    for idx, al in enumerate(available_lists):
        print(f"{idx+1}: {al['name'] or 'no name'}")

# Function to show available/selected labels
def show_labels():
    for idx, al in enumerate(available_labels):
        print(f"[{'x' if al['id'] in selected_label_ids else ' '}] Label {idx+1} - Name: {al['name'] or 'no name'} ({al['color']})")
    print("Type 'f' to finish the selection")

# Main part of the script
if __name__ == "__main__":
    # Getting Trello user (member) data
    print("Querying user (member) data...")
    member = get_me()
    # Now, we'll query the availble boards
    print("Querying available boards...")
    available_boards = get_boards(member['id'])

    # Selecting board where desired list (column) is located
    print('Please, select the board with the list in which the card must be inserted: ')
    while not selected_board:
        show_boards()
        tboard_idx = input()
        # Trying to get the selected option
        try:
            board_idx = int(tboard_idx)
            if board_idx >= 1 and board_idx <= len(available_boards) + 1:
                selected_board = available_boards[board_idx-1]
            # If user selects an invalid option
            else: print("Invalid option, please choose one of the available boards")
        # If an error occurs, it'll also be considered an invalid option
        except: print("Invalid option, please choose one of the available boards")
    
    # Now, we'll query the availble lists and labels
    print("Querying available lists...")
    available_lists = get_board_lists(selected_board['id'])
    print("Querying available labels...")
    available_labels = get_board_labels(selected_board['id'])

    # Selecting list (column) where to add the card
    print('Please, select the list in which the card must be inserted: ')
    while not selected_list:
        show_lists()
        tlist_idx = input()
        # Trying to get the selected option
        try:
            list_idx = int(tlist_idx)
            if list_idx >= 1 and list_idx <= len(available_lists) + 1:
                selected_list = available_lists[list_idx-1]
            # If user selects an invalid option
            else: print("Invalid option, please choose one of the available lists")
        # If an error occurs, it'll also be considered an invalid option
        except: print("Invalid option, please choose one of the available lists")

    # Card name and description
    name = input('Please, provide the name for the card to be created: ')
    while name == '':
        name = input("The card name cannot be empty, please, provide some text: ")
    desc = input('Please, provide the description for the card to be created (you can leave it empty): ')

    # Card labels
    add_labels_flag = None
    add_labels_flag = input('Would you like to add labels for the card? (y/n) ')
    while add_labels_flag not in ['y', 'n']:
        add_labels_flag = input("Invalid option, please type 'y' (for yes) or 'n' (for no) ").lower()
    
    # Requesting card labels (if required)
    if add_labels_flag == 'y':
        finish_label_selection = False
        print("Please, select the label(s) to be attached to the card: ")
        while not finish_label_selection:
            show_labels()
            tlabel_idx = input()
            # If user has finished selecting labels
            if tlabel_idx.lower() == 'f':
                finish_label_selection = True
                break
            # Trying to get the selected option
            try:
                label_idx = int(tlabel_idx)
                # We can either append or remove the item from the list
                if label_idx >= 1 and label_idx <= len(available_labels) + 1:
                    # Defining the label to be inserted/removed
                    current_label_id = available_labels[label_idx-1]['id']
                    if current_label_id not in selected_label_ids:
                        selected_label_ids.append(current_label_id)
                    else:
                        selected_label_ids.remove(current_label_id)
                # If user selects an invalid option
                else: print("Invalid option, please choose one of the available labels")
            # If an error occurs, it'll also be considered an invalid option
            except: print("Invalid option, please choose one of the available labels")
    
    # Card comment
    add_comment_flag = None
    add_comment_flag = input('Would you like to add a comment for the card? (y/n) ')
    while add_comment_flag not in ['y', 'n']:
        add_comment_flag = input("Invalid option, please type 'y' (for yes) or 'n' (for no) ").lower()

    # Requesting card comment (if required)
    comment = ''
    if add_comment_flag == 'y':
        comment = input("Please, provide the comment to be attached to the card: ")

    # Checking data with the user
    print("Please, check the provided data to see if it's all correct: ")
    print(f"- Selected board: {selected_board['name']}")
    print(f"- Selected list: {selected_list['name']}")
    print(f'- Card name: {name}')
    print(f'- Card description: {desc}')
    print('- Card labels:')
    for l in available_labels:
        if l['id'] in selected_label_ids:
            print(f" * Name: {l['name'] or 'no name'} ({l['color']})")
    print(f'- Card comment: {comment}')
    confirmation_flag = input("Is everything correct? (y/n) ").lower()
    while confirmation_flag not in ['y', 'n']:
        confirmation_flag = input("Invalid option, please type 'y' (for yes) or 'n' (for no) ").lower()
    
    # Finally, if everything is correct, we'll insert the card in the list
    if confirmation_flag == 'y':
        print("Creating new card...")
        card = post_card(selected_list['id'], name, desc, selected_label_ids)
        print("New card was successfully created!")
        # If a comment must be inserted
        if comment != '':
            print("Adding comment to the card...")
            new_comment = post_card_comment(card['id'], comment)
            print("Comment was successfully added to the card!")
    # IF user cancels, we inform about the cancelled operation
    else: print('Operation was cancelled.')
