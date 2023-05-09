Name:           android-simg2img
Version:        1.1.4
Release:        1%{?dist}
Summary:        Tool to convert Android sparse images to raw images

License:        ??
URL:            https://github.com/anestisb/android-simg2img
Source0:        https://github.com/anestisb/android-simg2img/archive/refs/tags/%{version}.tar.gz
Patch0:         https://github.com/anestisb/android-simg2img/commit/921d5be1c00d0a451597ffa705f24d8af08eabdd.diff
Patch1:         https://github.com/anestisb/android-simg2img/commit/49b5b2576867c68323552df074009ad99104adfa.diff

BuildRequires:  make
BuildRequires:  g++
BuildRequires: zlib-devel

%description
Tool to convert Android sparse images to raw images.

Since image tools are not part of Android SDK, this standalone port of AOSP libsparse aims to avoid complex building chains.

%prep
%autosetup


%build
%make_build


%install
%make_install
%{__install} -p -m 0755 -d %{buildroot}%{_bindir}/ %{buildroot}%{_includedir}/ %{buildroot}%{_libdir}/
mv %{buildroot}/usr/local/bin/* %{buildroot}%{_bindir}/
mv %{buildroot}/usr/local/include/* %{buildroot}%{_includedir}/
mv %{buildroot}/usr/local/lib/* %{buildroot}%{_libdir}/


%files
%{_bindir}/append2simg
%{_bindir}/img2simg
%{_bindir}/simg2img
%{_bindir}/simg2simg
%{_includedir}/sparse/sparse.h
%{_libdir}/libsparse.a


%changelog
* Tue May 09 2023 Markus Rathgeb <maggu2810@gmail.com>
- Initial RPM
