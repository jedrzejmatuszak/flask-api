from app.api import bp


# na POST tworzy nowy hit na podstawie przekazanego obiektu: artistID, title
@bp.route('/api/v1/hits')
def get_hits():
    pass


# można zaktualizować tylko: artistId, 'title' oraz 'title_url' + automatyczne
# wypełnienie pola updated_at
@bp.route('/api/v1/hits/<string:title_url>')
def get_title(title_url):
    pass


# usuwa wybrany hit
@bp.route('/api/v1/hits/<string:title_url>')
def delete_hit(title_url):
    pass
