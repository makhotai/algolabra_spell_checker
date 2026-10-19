from invoke import task

@task
def start(ctx):
    ctx.run("python src/app.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src/tests")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src/tests")
    ctx.run("coverage report")
    ctx.run("coverage html")

@task
def pylint(ctx):
    ctx.run("pylint src/services", pty=True)
