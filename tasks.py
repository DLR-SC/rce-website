from invoke import task, run
import os
import shutil
import sys
import socketserver

from pelican.server import ComplexHTTPRequestHandler

# Local path configuration (can be absolute or relative to fabfile)
deploy_path = 'output'

# Remote server configuration
production = 'root@localhost:22'
aest_path = '/var/www'

# Github Pages configuration
github_pages_branch = "gh-pages"

# Port for `serve`
PORT = 8001

@task
def clean(context):
    """Remove generated files"""
    if os.path.isdir(DEPLOY_PATH):
        shutil.rmtree(DEPLOY_PATH)
        os.makedirs(DEPLOY_PATH)

@task
def build(context):
    """Build local version of site"""
    run('pelican -s pelicanconf.py')

@task
def rebuild(context):
    """`clean` then `build`"""
    clean()
    build()

@task
def regenerate(context):
    """Automatically regenerate site upon file modification"""
    run('pelican -r -s pelicanconf.py')

@task
def serve(context):
    """Serve site at http://localhost:8000/"""
    os.chdir(deploy_path)

    class AddressReuseTCPServer(socketserver.TCPServer):
        allow_reuse_address = True

    # Pelican assumes that the request handler has a 'base_path' set.
    # Since this assumption does not hold true anymore, we set this
    # attribute here manually
    request_handler = ComplexHTTPRequestHandler
    request_handler.base_path = "."
    server = AddressReuseTCPServer(('', PORT), request_handler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

@task
def reserve(context):
    """`build`, then `serve`"""
    build()
    serve()

@task
def preview(context):
    """Build production version of site"""
    run('pelican -s publishconf.py')

@task
def gh_pages(context):
    """Publish to GitHub Pages"""
    clean()
    preview()
    local("ghp-import -b {github_pages_branch} {deploy_path}".format(**env))
    local("git push origin {github_pages_branch}".format(**env))
