Name:       kmod
Summary:    Linux kernel module handling
Version:    14
Release:    1
Group:      Kernel/Linux Kernel
License:    GPLv2
URL:        http://git.profusion.mobi/cgit.cgi/kmod.git/
Source0:    http://www.kernel.org/pub/linux/utils/kernel/kmod/%{name}-%{version}.tar.xz
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  libxslt
Provides:   module-init-tools > 3.15
Obsoletes:   module-init-tools <= 3.15

%description
kmod is a set of tools to handle common tasks with Linux kernel modules like
insert, remove, list, check properties, resolve dependencies and aliases.


%package libs
Summary:    Libraries for kmod
Group:      Kernel/Linux Kernel
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description libs
Libraries for kmod.

%package devel
Summary:    Devel files for libkmod
Group:      Kernel/Linux Kernel
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-libs = %{version}-%{release}

%description devel
Development files for libkmod.

%prep
%setup -q -n %{name}-%{version}/kmod/

%build
./bootstrap
%configure --disable-static \
    --with-xz \
    --with-zlib --disable-manpages

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

mkdir -p $RPM_BUILD_ROOT/sbin/
ln -sf %{_bindir}/kmod $RPM_BUILD_ROOT/sbin/modprobe
ln -sf %{_bindir}/kmod $RPM_BUILD_ROOT/sbin/modinfo
ln -sf %{_bindir}/kmod $RPM_BUILD_ROOT/sbin/insmod
ln -sf %{_bindir}/kmod $RPM_BUILD_ROOT/sbin/rmmod
ln -sf %{_bindir}/kmod $RPM_BUILD_ROOT/sbin/depmod
ln -sf %{_bindir}/kmod $RPM_BUILD_ROOT/sbin/lsmod

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/depmod.d
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/modprobe.d

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%dir %{_sysconfdir}/depmod.d
%dir %{_sysconfdir}/modprobe.d
%dir %{_prefix}/lib/modprobe.d
%{_bindir}/kmod
/sbin/modprobe
/sbin/modinfo
/sbin/insmod
/sbin/rmmod
/sbin/lsmod
/sbin/depmod
%{_datadir}/bash-completion/completions/kmod
#%attr(0644,root,root) %{_mandir}/man5/*.5*
#%attr(0644,root,root) %{_mandir}/man8/*.8*

%files libs
%defattr(-,root,root,-)
%{_libdir}/libkmod.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/libkmod.h
%{_libdir}/pkgconfig/libkmod.pc
%{_libdir}/libkmod.so

