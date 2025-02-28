# Calls بوت تشغيل اغاني بالتليقرام

## ✍🏻 Requirements

- FFmpeg
- Python 3.7+

## 🚀 Deployment

### 🛠 Configuration

1. Copy `example.env` to `.env` and fill it with your credentials.
2. Install Python requirements:
   ```bash
   pip install -U -r requirements.txt
   ```
3. Run:
   ```bash
   python -m callsmusic
   ```

### 🐬 Docker

1. Build:
   ```bash
   docker build -t musicplayer .
   ```
2. Run:
   ```bash
   docker run --env-file .env musicplayer
   ```

### 💜 Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/callsmusic/callsmusic)

## ℹ️ Commands

| Command | Description                                          |
| ------- | ---------------------------------------------------- |
| /play   | play the replied audio file or YouTube video         |
| /pause  | pause the audio stream                               |
| /resume | resume the audio stream                              |
| /skip   | skip the current audio stream                        |
| /mute   | mute the userbot                                     |
| /unmute | unmute the userbot                                   |
| /stop   | clear the queue and remove the userbot from the call |

## 📄 License

### GNU Affero General Public License v3.0-or-later

[Read more](http://www.gnu.org/licenses/#AGPL)

## ✨ Credits

- Il'ya ([tgcalls](https://github.com/MarshalX/tgcalls))
- Dan ([pyrogram](https://github.com/pyrogram/pyrogram))
