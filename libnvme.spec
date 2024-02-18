%global build_ldflags %{build_ldflags} -Wl,--undefined-version

%define major	1
%define libname %mklibname nvme%major
%define devname %mklibname nvme -d 

Name:		libnvme
Version:	1.8
Release:	1
Summary:	Native NVMe device management library
Group:		System/Kernel and hardware
License:	GPLv2+
URL:		https://github.com/linux-nvme/libnvme
Source0:	https://github.com/linux-nvme/libnvme/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	meson
BuildRequires:  cmake
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(json-c)
BuildRequires:	pkgconfig(libkeyutils)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(wheel)
BuildRequires:	pkgconfig(uuid)
# Disable swig as it cause problems with undefined symbol: _Py_Dealloc
BuildRequires:	swig

%package -n %{libname}
Summary:	Native NVMe device management library
Group:		System/Libraries

%package -n %{devname}
Summary:	Development libraries for libnvme
Group:		Development/C
Provides:	nvme-devel = %{EVRD}
Provides:	%{libname}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

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
 	-Dpython=disabled
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
