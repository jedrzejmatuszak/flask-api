from app.api import bp


# [GET] wyświetla listę 20 hitów
# [POST] tworzy nowy hit na podstawie przekazanego obiektu: artistID, title
"""
[
    {
        id: <hitId>,
        title: <title>,
        _titleUrl: <titleUrl>
    }
    {
        id: <hitId>,
        title: <title>,
        _titleUrl: <titleUrl>
    }
]
"""
@bp.route('/api/v1/hits', methods=['GET', 'POST'])
def get_hits():
    pass


# [GET] wyświetla szczegóły pojedynczego hitu
# [PUT] aktualizuje wybrany hit (tylko pola artist_id, title, title_url
# i automatycznie wypełnia pole updated_at
# [DELETE] usuwa wybrany hit
"""
{
    id: <hitId>,
    title: <title>,
    _titleUrl: <titleUrl>,
    createdAt: <createdAt>,
    artist: {
        id: <artistId>
        firstName: <firstName>
        lastName: <lastName>
    }
}
"""
@bp.route('/api/v1/hits/<string:title_url>', methods=['GET', 'PUT', 'DELETE'])
def get_title(title_url):
    pass
