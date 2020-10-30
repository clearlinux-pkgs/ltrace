#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ltrace
Version  : 0.7.3
Release  : 25
URL      : http://www.ltrace.org/ltrace_0.7.3.orig.tar.bz2
Source0  : http://www.ltrace.org/ltrace_0.7.3.orig.tar.bz2
Summary  : Tracks runtime library calls from dynamically linked executables.
Group    : Development/Tools
License  : GPL-2.0
Requires: ltrace-bin = %{version}-%{release}
Requires: ltrace-data = %{version}-%{release}
Requires: ltrace-license = %{version}-%{release}
Requires: ltrace-man = %{version}-%{release}
BuildRequires : dejagnu
BuildRequires : elfutils-dev
BuildRequires : expect
BuildRequires : libunwind-dev
BuildRequires : tcl
Patch1: ltrace-0.7.91-testsuite-includes.patch
Patch2: ltrace-0.7.91-testsuite-includes-2.patch

%description
Ltrace is a debugging program which runs a specified command until the
command exits.  While the command is executing, ltrace intercepts and
records both the dynamic library calls called by the executed process
and the signals received by the executed process.  Ltrace can also
intercept and print system calls executed by the process.

You should install ltrace if you need a sysadmin tool for tracking the
execution of processes.

%package bin
Summary: bin components for the ltrace package.
Group: Binaries
Requires: ltrace-data = %{version}-%{release}
Requires: ltrace-license = %{version}-%{release}

%description bin
bin components for the ltrace package.


%package data
Summary: data components for the ltrace package.
Group: Data

%description data
data components for the ltrace package.


%package doc
Summary: doc components for the ltrace package.
Group: Documentation
Requires: ltrace-man = %{version}-%{release}

%description doc
doc components for the ltrace package.


%package license
Summary: license components for the ltrace package.
Group: Default

%description license
license components for the ltrace package.


%package man
Summary: man components for the ltrace package.
Group: Default

%description man
man components for the ltrace package.


%prep
%setup -q -n ltrace-0.7.3
cd %{_builddir}/ltrace-0.7.3
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604100447
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --disable-static --sysconfdir=/usr/share/defaults/ltrace
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1604100447
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ltrace
cp %{_builddir}/ltrace-0.7.3/COPYING %{buildroot}/usr/share/package-licenses/ltrace/b47456e2c1f38c40346ff00db976a2badf36b5e3
cp %{_builddir}/ltrace-0.7.3/debian/copyright %{buildroot}/usr/share/package-licenses/ltrace/38566040a16c807f1c4f5f80894bb7909c6b439e
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ltrace

%files data
%defattr(-,root,root,-)
/usr/share/defaults/ltrace/ltrace.conf

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/ltrace/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ltrace/38566040a16c807f1c4f5f80894bb7909c6b439e
/usr/share/package-licenses/ltrace/b47456e2c1f38c40346ff00db976a2badf36b5e3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ltrace.1
/usr/share/man/man5/ltrace.conf.5
