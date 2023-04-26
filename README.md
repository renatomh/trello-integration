<h1 align="center"><img alt="Trello Integration" title="Trello Integration" src=".github/logo.png" width="250" /></h1>

# Trello Integration

## 💡 Project's Idea

This is a simple wrapper for the Trello REST API, in order to provide a CLI application to add Trello's cards to existing boards.

## 🔍 Features

* Creating new cards with labels and a comment to a specific board's column (list);

[![Watch the sample](https://img.youtube.com/vi/7zVomvIUkgE/0.jpg)](https://youtu.be/7zVomvIUkgE)

## 📝 Future Developemnt

Some interesting features which could be added to the application include:

* Creating new labels for the boards;
* Creating checklists for the cards;
* Adding stickers to the cards;
* Unit testing;
* Better input validation;

## 🛠 Technologies

During the development of this project, the following techologies were used:

- [Python](https://www.python.org/)
- [Trello API](https://developer.atlassian.com/cloud/trello/rest/api-group-actions/)

## 💻 Project Configuration

### Make sure to install the required packages/libs before running the script

```bash
$ pip install -r requirements.txt
```

You must also update the [config,py](./config.py) file with your API key and token, in order to use the application (get yours [here](https://trello.com/power-ups/admin)).

```python
TRELLO_API_KEY = 'YOUR_TRELLO_API_KEY'
TRELLO_TOKEN = 'YOUR_TRELLO_TOKEN'
```

## ⏯️ Running

To run the application locally, execute the following command on the root directory.

```bash
$ python add_card
```

### Documentation:
* [Trello API - Create a new Card](https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-post)
* [Trello API - Create a Label](https://developer.atlassian.com/cloud/trello/rest/api-group-labels/#api-labels-post)
* [Trello API - Create a new Label on a Card](https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-id-labels-post)
* [Trello API - Add a new comment to a Card](https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-id-actions-comments-post)

## 📄 License

This project is under the **MIT** license. For more information, access [LICENSE](./LICENSE).
