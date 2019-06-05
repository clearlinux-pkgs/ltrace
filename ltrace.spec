#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ltrace
Version  : 0.7.3
Release  : 24
URL      : http://www.ltrace.org/ltrace_0.7.3.orig.tar.bz2
Source0  : http://www.ltrace.org/ltrace_0.7.3.orig.tar.bz2
Summary  : Tracks runtime library calls from dynamically linked executables.
Group    : Development/Tools
License  : GPL-2.0
Requires: ltrace-bin
Requires: ltrace-data
Requires: ltrace-doc
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
Requires: ltrace-data

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

%description doc
doc components for the ltrace package.


%prep
%setup -q -n ltrace-0.7.3
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519866935
%configure --disable-static --disable-static --sysconfdir=/usr/share/defaults/ltrace
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1519866935
rm -rf %{buildroot}
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
%defattr(-,root,root,-)
%doc /usr/share/doc/ltrace/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
