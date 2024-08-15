#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
Name     : fastfetch
Version  : 2.21.3
Release  : 10
URL      : https://github.com/fastfetch-cli/fastfetch/archive/2.21.3/fastfetch-2.21.3.tar.gz
Source0  : https://github.com/fastfetch-cli/fastfetch/archive/2.21.3/fastfetch-2.21.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: fastfetch-bin = %{version}-%{release}
Requires: fastfetch-data = %{version}-%{release}
Requires: fastfetch-license = %{version}-%{release}
Requires: fastfetch-man = %{version}-%{release}
BuildRequires : Vulkan-Headers-dev
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(DirectX-Headers)
BuildRequires : pkgconfig(ImageMagick)
BuildRequires : pkgconfig(OpenCL)
BuildRequires : pkgconfig(chafa)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(dconf)
BuildRequires : pkgconfig(ddcutil)
BuildRequires : pkgconfig(dri)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libnm)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libxfconf-0)
BuildRequires : pkgconfig(osmesa)
BuildRequires : pkgconfig(rpm)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(vulkan)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xcb-randr)
BuildRequires : pkgconfig(xrandr)
BuildRequires : pkgconfig(zlib)
BuildRequires : python3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Fastfetch
[![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/fastfetch-cli/fastfetch/ci.yml)](https://github.com/fastfetch-cli/fastfetch/actions)
[![GitHub license](https://img.shields.io/github/license/fastfetch-cli/fastfetch)](https://github.com/fastfetch-cli/fastfetch/blob/dev/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/fastfetch-cli/fastfetch)](https://github.com/fastfetch-cli/fastfetch/graphs/contributors)
[![GitHub top language](https://img.shields.io/github/languages/top/fastfetch-cli/fastfetch?logo=c&label=)](https://github.com/fastfetch-cli/fastfetch/blob/dev/CMakeLists.txt#L5)
[![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/m/fastfetch-cli/fastfetch)](https://github.com/fastfetch-cli/fastfetch/commits)
[![homebrew downloads](https://img.shields.io/homebrew/installs/dm/fastfetch?logo=homebrew)](https://formulae.brew.sh/formula/fastfetch#default)
[![GitHub all releases](https://img.shields.io/github/downloads/fastfetch-cli/fastfetch/total?logo=github)](https://github.com/fastfetch-cli/fastfetch/releases)
[![GitHub release (with filter)](https://img.shields.io/github/v/release/fastfetch-cli/fastfetch?logo=github)](https://github.com/fastfetch-cli/fastfetch/releases)
[![latest packaged version(s)](https://repology.org/badge/latest-versions/fastfetch.svg)](https://repology.org/project/fastfetch/versions)
[![Packaging status](https://repology.org/badge/tiny-repos/fastfetch.svg)](https://repology.org/project/fastfetch/versions)

%package bin
Summary: bin components for the fastfetch package.
Group: Binaries
Requires: fastfetch-data = %{version}-%{release}
Requires: fastfetch-license = %{version}-%{release}

%description bin
bin components for the fastfetch package.


%package data
Summary: data components for the fastfetch package.
Group: Data

%description data
data components for the fastfetch package.


%package license
Summary: license components for the fastfetch package.
Group: Default

%description license
license components for the fastfetch package.


%package man
Summary: man components for the fastfetch package.
Group: Default

%description man
man components for the fastfetch package.


%prep
%setup -q -n fastfetch-2.21.3
cd %{_builddir}/fastfetch-2.21.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1723718668
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1723718668
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fastfetch
cp %{_builddir}/fastfetch-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/fastfetch/ed9c8efe6c67cf1f74819436927814a0b31b8ef7 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fastfetch
/usr/bin/flashfetch

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/fastfetch
/usr/share/fastfetch/presets/all.jsonc
/usr/share/fastfetch/presets/archey.jsonc
/usr/share/fastfetch/presets/ci.jsonc
/usr/share/fastfetch/presets/examples/10.jsonc
/usr/share/fastfetch/presets/examples/11.jsonc
/usr/share/fastfetch/presets/examples/12.jsonc
/usr/share/fastfetch/presets/examples/13.jsonc
/usr/share/fastfetch/presets/examples/14.jsonc
/usr/share/fastfetch/presets/examples/15.jsonc
/usr/share/fastfetch/presets/examples/16.jsonc
/usr/share/fastfetch/presets/examples/17.jsonc
/usr/share/fastfetch/presets/examples/18.jsonc
/usr/share/fastfetch/presets/examples/19.jsonc
/usr/share/fastfetch/presets/examples/2.jsonc
/usr/share/fastfetch/presets/examples/20.jsonc
/usr/share/fastfetch/presets/examples/21.jsonc
/usr/share/fastfetch/presets/examples/22.jsonc
/usr/share/fastfetch/presets/examples/23.jsonc
/usr/share/fastfetch/presets/examples/3.jsonc
/usr/share/fastfetch/presets/examples/4.jsonc
/usr/share/fastfetch/presets/examples/5.jsonc
/usr/share/fastfetch/presets/examples/6.jsonc
/usr/share/fastfetch/presets/examples/7.jsonc
/usr/share/fastfetch/presets/examples/8.jsonc
/usr/share/fastfetch/presets/examples/9.jsonc
/usr/share/fastfetch/presets/neofetch.jsonc
/usr/share/fastfetch/presets/paleofetch.jsonc
/usr/share/fastfetch/presets/screenfetch.jsonc
/usr/share/fish/vendor_completions.d/fastfetch.fish
/usr/share/licenses/fastfetch/LICENSE

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fastfetch/ed9c8efe6c67cf1f74819436927814a0b31b8ef7

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/fastfetch.1
