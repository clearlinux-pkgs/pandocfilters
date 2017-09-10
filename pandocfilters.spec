#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pandocfilters
Version  : 1.4.2
Release  : 4
URL      : https://pypi.debian.net/pandocfilters/pandocfilters-1.4.2.tar.gz
Source0  : https://pypi.debian.net/pandocfilters/pandocfilters-1.4.2.tar.gz
Summary  : Utilities for writing pandoc filters in python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pandocfilters-legacypython
Requires: pandocfilters-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=============

%package legacypython
Summary: legacypython components for the pandocfilters package.
Group: Default

%description legacypython
legacypython components for the pandocfilters package.


%package python
Summary: python components for the pandocfilters package.
Group: Default
Requires: pandocfilters-legacypython

%description python
python components for the pandocfilters package.


%prep
%setup -q -n pandocfilters-1.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505010825
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1505010825
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
