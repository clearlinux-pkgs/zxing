#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe40c24
#
Name     : zxing
Version  : 2.2.0
Release  : 7
URL      : https://github.com/zxing-cpp/zxing-cpp/archive/v2.2.0/zxing-cpp-2.2.0.tar.gz
Source0  : https://github.com/zxing-cpp/zxing-cpp/archive/v2.2.0/zxing-cpp-2.2.0.tar.gz
Source1  : https://github.com/nothings/stb/archive/8b5f1f37b5b75829fc72d38e7b5d4bcbf8a26d55/stb-8b5f1f3.tar.gz
Summary  : ZXing-C++ library
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: zxing-lib = %{version}-%{release}
Requires: zxing-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : opencv-dev
BuildRequires : pkg-config
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![Build Status](https://github.com/zxing-cpp/zxing-cpp/workflows/CI/badge.svg?branch=master)](https://github.com/zxing-cpp/zxing-cpp/actions?query=workflow%3ACI)

%package dev
Summary: dev components for the zxing package.
Group: Development
Requires: zxing-lib = %{version}-%{release}
Provides: zxing-devel = %{version}-%{release}
Requires: zxing = %{version}-%{release}

%description dev
dev components for the zxing package.


%package lib
Summary: lib components for the zxing package.
Group: Libraries
Requires: zxing-license = %{version}-%{release}

%description lib
lib components for the zxing package.


%package license
Summary: license components for the zxing package.
Group: Default

%description license
license components for the zxing package.


%prep
%setup -q -n zxing-cpp-2.2.0
cd %{_builddir}
tar xf %{_sourcedir}/stb-8b5f1f3.tar.gz
cd %{_builddir}/zxing-cpp-2.2.0
mkdir -p stb
cp -r %{_builddir}/stb-8b5f1f37b5b75829fc72d38e7b5d4bcbf8a26d55/* %{_builddir}/zxing-cpp-2.2.0/stb

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702075254
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
%cmake .. -DBUILD_EXAMPLES=OFF \
-DBUILD_BLACKBOX_TESTS=OFF \
-Dstb_SOURCE_DIR=..
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

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
export SOURCE_DATE_EPOCH=1702075254
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zxing
cp %{_builddir}/stb-8b5f1f37b5b75829fc72d38e7b5d4bcbf8a26d55/LICENSE %{buildroot}/usr/share/package-licenses/zxing/b725e4c292b2ad7fdcc0747c986495176f99cdb3 || :
cp %{_builddir}/zxing-cpp-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/zxing/669a1e53b9dd9df3474300d3d959bb85bad75945 || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/ZXing/BarcodeFormat.h
/usr/include/ZXing/BitHacks.h
/usr/include/ZXing/BitMatrix.h
/usr/include/ZXing/BitMatrixIO.h
/usr/include/ZXing/ByteArray.h
/usr/include/ZXing/CharacterSet.h
/usr/include/ZXing/Content.h
/usr/include/ZXing/DecodeHints.h
/usr/include/ZXing/Error.h
/usr/include/ZXing/Flags.h
/usr/include/ZXing/GTIN.h
/usr/include/ZXing/ImageView.h
/usr/include/ZXing/Matrix.h
/usr/include/ZXing/MultiFormatWriter.h
/usr/include/ZXing/Point.h
/usr/include/ZXing/Quadrilateral.h
/usr/include/ZXing/Range.h
/usr/include/ZXing/ReadBarcode.h
/usr/include/ZXing/ReaderOptions.h
/usr/include/ZXing/Result.h
/usr/include/ZXing/StructuredAppend.h
/usr/include/ZXing/TextUtfEncoding.h
/usr/include/ZXing/ZXAlgorithms.h
/usr/include/ZXing/ZXConfig.h
/usr/include/ZXing/ZXVersion.h
/usr/lib64/cmake/ZXing/ZXingConfig.cmake
/usr/lib64/cmake/ZXing/ZXingConfigVersion.cmake
/usr/lib64/cmake/ZXing/ZXingTargets-relwithdebinfo.cmake
/usr/lib64/cmake/ZXing/ZXingTargets.cmake
/usr/lib64/libZXing.so
/usr/lib64/pkgconfig/zxing.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libZXing.so.2.2.0
/usr/lib64/libZXing.so.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zxing/669a1e53b9dd9df3474300d3d959bb85bad75945
/usr/share/package-licenses/zxing/b725e4c292b2ad7fdcc0747c986495176f99cdb3
