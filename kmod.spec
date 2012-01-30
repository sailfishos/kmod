# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.23
# 
# >> macros
# << macros

Name:       kmod
Summary:    Linux kernel module handling
Version:    4
Release:    1
Group:      Kernel/Linux Kernel
License:    LGPLv2
URL:        http://git.profusion.mobi/cgit.cgi/kmod.git/
Source0:    http://packages.profusion.mobi/kmod/%{name}-%{version}.tar.xz
Source100:  kmod.yaml
BuildRequires:  pkgconfig(zlib)
BuildRequires:  lzo-devel


%description
kmod is a set of tools to handle common tasks with Linux kernel modules like
insert, remove, list, check properties, resolve dependencies and aliases.



%package devel
Summary:    Devel files for libkmod
Group:      Kernel/Linux Kernel
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-libs = %{version}-%{release}

%description devel
Development files for libkmod.

%package libs
Summary:    kmod libraries
Group:      Kernel/Linux Kernel
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description libs
Libraries for kmod.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post










%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/kmod
%{_mandir}/*
# >> files
# << files


%files devel
%defattr(-,root,root,-)
%{_includedir}/libkmod.h
%{_libdir}/libkmod.so
%{_libdir}/pkgconfig/libkmod.pc
# >> files devel
# << files devel

%files libs
%defattr(-,root,root,-)
%{_libdir}/libkmod.so.*
# >> files libs
# << files libs

