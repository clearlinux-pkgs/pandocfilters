#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pandocfilters
Version  : 1.4.2
Release  : 10
URL      : https://pypi.debian.net/pandocfilters/pandocfilters-1.4.2.tar.gz
Source0  : https://pypi.debian.net/pandocfilters/pandocfilters-1.4.2.tar.gz
Summary  : Utilities for writing pandoc filters in python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pandocfilters-python3
Requires: pandocfilters-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=============

%package python
Summary: python components for the pandocfilters package.
Group: Default
Requires: pandocfilters-python3

%description python
python components for the pandocfilters package.


%package python3
Summary: python3 components for the pandocfilters package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pandocfilters package.


%prep
%setup -q -n pandocfilters-1.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523295864
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
