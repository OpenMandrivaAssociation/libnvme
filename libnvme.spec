%define rel 1
%define major	1
%define libname %mklibname nvme%major
%define devname %mklibname nvme -d 

Name:		libnvme
Version:	1.2
Release:	%mkrel %{rel}
Summary:	Native NVMe device management library
Group:		System/Kernel and hardware
License:	GPLv2+
URL:		https://github.com/linux-nvme/libnvme
Source0:	https://github.com/linux-nvme/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	meson >= 0.47.0
BuildRequires:	pkgconfig(json-c)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(uuid)
# To fix: for python bindings swig is required (actually doesn't work, is it broken our swig package?)
#BuildRequires:	swig

%package -n %{libname}
Summary:	Native NVMe device management library
Group:		System/Libraries

%package -n %{devname}
Summary:	Development libraries for libnvme
Group:		Development/C
Provides:	nvme-devel = %{version}-%{release}
Provides:	%{libname}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description
A library for accessing to NVMe under linux.

%description -n %{libname}
libnvme is library for accessing to NVMe under linux.

%description -n %{devname}
Header files and libraries needed to develop programs that use the libnvme
library.

%prep
%setup -q
%autopatch -p1

%build
%meson \
	-Ddocs=man \
	-Ddocs-build=true \
%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/*.so.%{major}{,.*}

%files -n %{devname}
%doc README.md
%license COPYING
%{_libdir}/lib*.so
%{_includedir}/*.h
%{_includedir}/nvme
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man2/*
