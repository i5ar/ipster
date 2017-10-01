def main():
    readme_in = 'README.md'
    readme_out = 'README.rst'
    try:
        from pypandoc import convert_file
        readme = convert_file(readme_in, 'rst')
        with open(readme_out, 'w') as f:
            f.write(readme)
    except ImportError as e:
        print(e)
