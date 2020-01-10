Name: mythes-mi
Summary: Maori thesaurus
%define upstreamid 20080630
Version: 0.%{upstreamid}
Release: 9%{?dist}
Source: http://packages.papakupu.maori.nz/mythes/mythes-mi-0.1.%{upstreamid}-beta.tar.gz
Group: Applications/Text
URL: http://papakupu.maori.nz/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: Public Domain
BuildArch: noarch
Requires: mythes

%description
Maori thesaurus.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p mi.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_mi_NZ_v2.dat
cp -p mi.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_mi_NZ_v2.idx

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc mi.AUTHORS mi.README mi.LICENSE
%{_datadir}/mythes/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.20080630-9
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080630-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080630-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080630-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080630-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Apr 04 2010 Caolan McNamara <caolanm@redhat.com> - 0.20080630-4
- mythes now owns /usr/share/mythes

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080630-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080630-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Caolan McNamara <caolanm@redhat.com> - 0.20080630-1
- initial version
