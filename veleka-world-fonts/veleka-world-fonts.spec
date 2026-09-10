Name:           veleka-world-fonts
Version:        1.0.0
Release:        0
Summary:        Serif font family with Bulgarian-style Cyrillic
License:        OFL-1.1
URL:            https://github.com/eniac111/Veleka
#!RemoteAsset: sha256:5d70df46c01ef96dffc82400b0c628804dccf15f455fc9e41c9a7947f43406eb
Source0:        https://github.com/eniac111/Veleka/releases/download/v%{version}/%{name}-%{version}.zip
BuildArch:      noarch
BuildRequires:  unzip
%if 0%{?suse_version}
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
%global fontdir %{_ttfontsdir}
%else
%global fontdir %{_datadir}/fonts/veleka-world
%endif

%description
Veleka World is a serif font family by Stefan Peev, part of the LOCAL FONTS
project. It is derived from Charis SIL and covers Latin, Greek, Cyrillic and
IPA. Applications show the Bulgarian forms of Cyrillic letters for text
marked as Bulgarian, or in any language with stylistic set 1.

%prep
%autosetup -c

%build

%install
install -d %{buildroot}%{fontdir}
install -p -m 0644 *.otf %{buildroot}%{fontdir}/

%if 0%{?suse_version}
%reconfigure_fonts_scriptlets
%endif

%files
%license OFL.txt
%dir %{fontdir}
%{fontdir}/*.otf

%changelog
* Thu Sep 10 2026 Blagovest Petrov <blagovest@petrovs.info> - 1.0.0-0
- Initial package
