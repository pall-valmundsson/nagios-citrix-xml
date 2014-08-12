Name:		nagios-plugin-citrix-xml
Version:	0.3
Release:	1%{?dist}
Summary:	A Nagios plugin to check the response from a Citrix XML Service

Group:		Applications/System
License:	GPLv3+
URL:		https://github.com/pall-valmundsson/nagios-citrix-xml
Source0:	%{name}-%{version}.tar.gz

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:	pynag >= 0.9.1


%description
A Nagios plugin to check the response from a Citrix XML Service

%prep
%setup -q


%build


%install
test "x$RPM_BUILD_ROOT" != "x" && rm -rf $RPM_BUILD_ROOT
install -D -p -m 755 check_citrix-xml %{buildroot}%{_libdir}/nagios/plugins/check_citrix-xml

%files
%doc README.md LICENSE
%{_libdir}/nagios/plugins/check_citrix-xml


%changelog
* Tue Aug 12 2014 Pall Valmundsson <pall.valmundsson@gmail.com> 0.3-1
- Python 2.6 compatibility fix

* Tue Aug 12 2014 Pall Valmundsson <pall.valmundsson@gmail.com> 0.2-1
- Catch HTTP errors from XML service

* Mon Aug 11 2014 Pall Valmundsson <pall.valmundsson@gmail.com> 0.1-1
- Initial release
