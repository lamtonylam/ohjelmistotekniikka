from invoke import task


@task
def build(ctx):
    ctx.run("python3 src/build.py", pty=True)


@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)


@task
def test(ctx):
    ctx.run("pytest -p no:warnings src", pty=True)


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest -p no:warnings src", pty=True)


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)


@task
def lint(ctx):
    ctx.run("pylint src", pty=True)


@task
def docstring(ctx):
    ctx.run("poetry run interrogate -v src/", pty=True)


@task(coverage_report)
def coverage_image(ctx):
    ctx.run("coverage-badge -o dokumentaatio/kuvat/coverage.svg -f", pty=True)
    ctx.run(
        "weasyprint htmlcov/index.html dokumentaatio/kuvat/coverage_report.pdf",
        pty=True,
    )
    ctx.run("python3 dokumentaatio/pdf_to_html.py", pty=True)
    ctx.run("rm -rf dokumentaatio/kuvat/coverage_report.pdf", pty=True)
