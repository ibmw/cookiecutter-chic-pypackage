# Installation

## Stable release

To install {{ cookiecutter.package_name }}, run this command in your
terminal:

``` console
pip install {{ cookiecutter.package_name|slugify }}
```

This is the preferred method to install {{ cookiecutter.package_name
}}, as it will always install the most recent stable release.

If you don't have [pip][] installed, this [Python installation guide][]
can guide you through the process.

## From source

The source for {{ cookiecutter.package_name }} can be downloaded from
the [Github repo][].

You can either clone the public repository:

``` console
git clone git://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name|slugify }}
```

Or download the [tarball][]:

``` console
curl -OJL https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name|slugify }}/tarball/master
```

Once you have a copy of the source, you can install it with:

``` console
pip install .
```

  [pip]: https://pip.pypa.io
  [Python installation guide]: http://docs.python-guide.org/en/latest/starting/installation/
  [Github repo]: https://github.com/%7B%7B%20cookiecutter.github_username%20%7D%7D/%7B%7B%20cookiecutter.package_name|slugify%20%7D%7D
  [tarball]: https://github.com/%7B%7B%20cookiecutter.github_username%20%7D%7D/%7B%7B%20cookiecutter.package_name|slugify%20%7D%7D/tarball/master
