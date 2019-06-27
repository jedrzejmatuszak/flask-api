from app.api import bp


@bp.route('/api/v1/hits')
def get_hits():
    pass


@bp.route('/api/v1/hits/<string:title_url>')
def get_title(title_url):
    pass