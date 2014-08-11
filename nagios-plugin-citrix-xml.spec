Name:		nagios-plugin-citrix-xml
Version:	0.1
Release:	1%{?dist}
Summary:	A Nagios plugin to check the response from a Citrix XML Broker

Group:		Applications/System
License:	GPLv3+
URL:		https://github.com/pall-valmundsson/nagios-plugin-citrix-xml
Source0:	https://github.com/pall-valmundsson/nagios-plugin-citrix-xml/archive/v%{version}.tar.gz

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:	pynag >= 0.9.1


%description
A Nagios plugin to check the response from a Citrix XML Broker

%prep
%setup -q


%build


%install
test "x$RPM_BUILD_ROOT" != "x" && rm -rf $RPM_BUILD_ROOT
install -D -p -m 755 check_citrix-xml %{buildroot}%{_libdir}/nagios/plugins/check_citrix-xml

%files
%doc README LICENSE
%{_libdir}/nagios/plugins/check_citrix-xml


%changelog
* Mon Aug 11 2014 Pall Valmundsson <pall.valmundsson@gmail.com> 0.1-1
- Initial release
