"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "Playlists"

     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)

    songs = db.relationship('Song',
                            secondary='playlists_songs',
                            backref='playlists')

    def __repr__(self):
        return f"<Playlist {self.name}>"



class Song(db.Model):
    """Song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "Songs"


    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    artist = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Song {self.title} - {self.artist}>"



class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE
        __tablename__ = "Playlist Songs"


    __tablename__ = "playlists_songs"

    id = db.Column(db.Integer, primarykey=True, autoincrement=True)
    song_id = db.Column(db.Integer,
                        db.ForeignKey("songs.id"))
    playlist_id = db.Column(db.Integer,
                            db.ForeignKey("playlists.id"))



# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
