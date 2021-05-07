#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pandocfilters
Version  : 1.4.2
Release  : 32
URL      : https://pypi.debian.net/pandocfilters/pandocfilters-1.4.2.tar.gz
Source0  : https://pypi.debian.net/pandocfilters/pandocfilters-1.4.2.tar.gz
Summary  : Utilities for writing pandoc filters in python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pandocfilters-license = %{version}-%{release}
Requires: pandocfilters-python = %{version}-%{release}
Requires: pandocfilters-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
=============

%package license
Summary: license components for the pandocfilters package.
Group: Default

%description license
license components for the pandocfilters package.


%package python
Summary: python components for the pandocfilters package.
Group: Default
Requires: pandocfilters-python3 = %{version}-%{release}

%description python
python components for the pandocfilters package.


%package python3
Summary: python3 components for the pandocfilters package.
Group: Default
Requires: python3-core
Provides: pypi(pandocfilters)

%description python3
python3 components for the pandocfilters package.


%prep
%setup -q -n pandocfilters-1.4.2
cd %{_builddir}/pandocfilters-1.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603397523
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pandocfilters
cp %{_builddir}/pandocfilters-1.4.2/LICENSE %{buildroot}/usr/share/package-licenses/pandocfilters/9990e0fc59b210f7995dbe22caeb082cae511080
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pandocfilters/9990e0fc59b210f7995dbe22caeb082cae511080

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
