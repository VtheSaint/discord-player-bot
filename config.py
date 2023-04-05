# token must be changed
music_token = "MTA5MjQ5ODc0ODA3ODMwOTM3Ng.GgHkat.jRyO3Uc8bjjGkLHJTkJAqx5FtQWY18LcJju-bc"

YTDL_OPTIONS = {'format': 'bestaudio/best', 'noplaylist': True,
                'simulate': True, 'key': 'FFmpegExtractAudio', 'forceduration': True, 'quiet': True, 'no_warnings': True}
FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

categories_ids = {569924343010689025: 1012127570260668416}

admin_ids = {569924343010689025: [
    332205797960450049, 301870946208448512, 271997864027095050]}

log_ids = {569924343010689025: 609820291669033026, 1087829089735430144: 1089856188067356713}

welcome_ids = {569924343010689025: 569927228624863252}


embed_colors = {"songs": [0, 0, 0], "member_action": [
    255, 255, 255], "other_action": [160, 220, 255], "switched_vc": [255, 180, 255], "joined_vc": [0, 255, 0], "left_vc": [255, 0, 0], "voice_update": [255, 255, 0]}

radio_url = "https://pool.anison.fm/AniSonFM(128)"