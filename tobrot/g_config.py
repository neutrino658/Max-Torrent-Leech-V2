from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
	TG_BOT_TOKEN= "1501108805:AAHKDmdzjsJE3VhiKw9E_TQjFjk_bDltPvA"
	APP_ID = 2159883
	API_HASH = "21e4ac78852e9ace0ccf3a2a4beb994f"
	OWNER_ID = "1281593392" #ID of bot owner
	AUTH_CHANNEL = [-519397713]
	DESTINATION_FOLDER = "MyTorrent" #Name of your folder read readme
	RCLONE_CONFIG = """type = drive\nscope = drive\ntoken = {"access_token": "ya29.A0AfH6SMBYnl9pC2x93EPFtMJqbGLk1PkyV5Psrbk4gnH3fuIYDKGgOK_gWpyhk7X0fYd5J7vpk4HGffiUROtyc9qdENeGU4urbwt9Tx3fZ1y-2i0Hlc4-0jK5c-fRLyZdyTXau_H3uxv7bZ7UJFc72QPvkON5", "client_id": "621284572381-0dpa3c7vrt1f7qkqeet9rgmg1fadqptg.apps.googleusercontent.com", "client_secret": "nZPkynAH0U3s1U2lGmzhVAVy", "refresh_token": "1//04BBEWYwncNWvCgYIARAAGAQSNwF-L9IrcXzUiL17Q2MVLwJuiMcD8LUIE6CSbMdCDSP5C_Z-yiAI_mT8ucBSPu2wHYL__T7HPi0", "token_expiry": "2021-01-26T11:44:59Z", "token_uri": "https://oauth2.googleapis.com/token", "user_agent": null, "revoke_uri": "https://oauth2.googleapis.com/revoke", "id_token": null, "id_token_jwt": null, "token_response": {"access_token": "ya29.A0AfH6SMBYnl9pC2x93EPFtMJqbGLk1PkyV5Psrbk4gnH3fuIYDKGgOK_gWpyhk7X0fYd5J7vpk4HGffiUROtyc9qdENeGU4urbwt9Tx3fZ1y-2i0Hlc4-0jK5c-fRLyZdyTXau_H3uxv7bZ7UJFc72QPvkON5", "expires_in": 3599, "refresh_token": "1//04BBEWYwncNWvCgYIARAAGAQSNwF-L9IrcXzUiL17Q2MVLwJuiMcD8LUIE6CSbMdCDSP5C_Z-yiAI_mT8ucBSPu2wHYL__T7HPi0", "scope": "https://www.googleapis.com/auth/drive", "token_type": "Bearer"}, "scopes": ["https://www.googleapis.com/auth/drive"], "token_info_uri": "https://oauth2.googleapis.com/tokeninfo", "invalid": false, "_class": "OAuth2Credentials", "_module": "oauth2client.client"}"""
	#fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
