const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});

await lib.discord.channels['@0.3.2'].messages.create({
  "channel_id": `${context.params.event.channel_id}`,
  "content": "",
  "tts": false,
  "components": [
    {
      "type": 1,
      "components": [
        {
          "custom_id": `row_0_select_0`,
          "placeholder": `Select player statistics you would like to view`,
          "options": [
            {
              "label": `All Statistics`,
              "value": `0`,
              "description": `View all player statistics in the database`,
              "emoji": {
                "id": null,
                "name": `📚`
              },
              "default": true
            },
            {
              "label": `Tickets Owned`,
              "value": `1`,
              "description": `View player tickets owned`,
              "emoji": {
                "id": null,
                "name": `🎟`
              },
              "default": false
            },
            {
              "label": `Token Balances`,
              "value": `2`,
              "description": `View player tokens amount and cash out amount`,
              "emoji": {
                "id": null,
                "name": `✨`
              },
              "default": false
            },
            {
              "label": `Player Meta Data`,
              "value": `3`,
              "description": `Player meta data like total wins, net worth, etc`,
              "emoji": {
                "id": null,
                "name": `📟`
              },
              "default": false
            }
          ],
          "min_values": 1,
          "max_values": 1,
          "type": 3
        }
      ]
    },
    {
      "type": 1,
      "components": [
        {
          "style": 4,
          "label": `Buy Small Ticket 🎟️`,
          "custom_id": `row_1_button_0`,
          "disabled": false,
          "emoji": {
            "id": null,
            "name": `🔺`
          },
          "type": 2
        },
        {
          "style": 3,
          "label": `Buy Large Ticket 🎟️`,
          "custom_id": `row_1_button_1`,
          "disabled": false,
          "emoji": {
            "id": null,
            "name": `🧧`
          },
          "type": 2
        },
        {
          "style": 2,
          "label": `Request Cash Out`,
          "custom_id": `row_1_button_2`,
          "disabled": false,
          "emoji": {
            "id": null,
            "name": `💸`
          },
          "type": 2
        }
      ]
    }
  ],
  "message_reference": {
    "message_id": "0000 ID of the original message 0000",
    "fail_if_not_exists": true
  },
  "allowed_mentions": {
    "replied_user": false,
    "parse": [
      "roles"
    ],
    "roles": [
      "Insert Lottery Role"
    ]
  },
  "embeds": [
    {
      "type": "rich",
      "title": "",
      "description": "",
      "color": 0xf76402,
      "timestamp": `2001-01-01T06:00:00.000Z`,
      "image": {
        "url": `https://media.tenor.com/ysaHf9PC5G4AAAAC/cyberpunk2077-jackie.gif`,
        "height": 460,
        "width": 260
      },
      "author": {
        "name": `Author Name`,
        "icon_url": `https://images.pexels.com/photos/270815/pexels-photo-270815.jpeg?cs=srgb&dl=pexels-pixabay-270815.jpg&fm=jpg`
      },
      "footer": {
        "text": `Net Worth`,
        "icon_url": `https://images.pexels.com/photos/270815/pexels-photo-270815.jpeg?cs=srgb&dl=pexels-pixabay-270815.jpg&fm=jpg`
      }
    }
  ]
});




const lib = require('lib')({token: process.env.STDLIB_SECRET_TOKEN});

await lib.discord.commands['@0.0.0'].create({
  "name": "lottery",
  "description": "Open the general tab for buying tickets and viewing your statistics",
  "options": []
});