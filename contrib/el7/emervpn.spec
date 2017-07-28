Name:           emervpn
Version:        1.0
Release:        1%{?dist}
Summary:        EmerVPN Service
Group:          Applications/Internet
Vendor:         Aspanta Limited
License:        MIT
URL:            http://www.emercoin.com
Source0:        %{name}.tar.gz
BuildArch:      noarch
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires:       openvpn emercoin emcssh iptables

%description
EmerVPN Service

%prep
%setup -q -n emervpn

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT/etc/emervpn $RPM_BUILD_ROOT/etc/emercoin/emcssh.keys.d $RPM_BUILD_ROOT/etc/sudoers.d $RPM_BUILD_ROOT/etc/sysctl.d $RPM_BUILD_ROOT/lib/systemd/system
%{__cp} -rf configs/emervpn/* $RPM_BUILD_ROOT/etc/emervpn
%{__cp} -rf configs/emcssh/* $RPM_BUILD_ROOT/etc/emercoin/emcssh.keys.d
%{__cp} -rf configs/sudoers/* $RPM_BUILD_ROOT/etc/sudoers.d
%{__cp} -rf configs/sysctl/* $RPM_BUILD_ROOT/etc/sysctl.d
%{__cp} -rf configs/systemd/* $RPM_BUILD_ROOT/lib/systemd/system

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%posttrans
sysctl -p /etc/sysctl.d/emervpn.conf >/dev/null 2>&1 || true
systemctl daemon-reload >/dev/null 2>&1 || true
systemctl restart emervpn >/dev/null 2>&1 || true
systemctl enable emervpn >/dev/null 2>&1 || true

%files
%defattr(-,root,root)
%config(noreplace) /etc/emervpn/*
%config(noreplace) /etc/emercoin/emcssh.keys.d/*
/etc/sudoers.d/*
/etc/sysctl.d/*
/lib/systemd/system/*

%changelog
* Fri Jul 28 2017 Sergii Vakula <sv@aspanta.com> 1.0
- There is no changelog availavle. Please refer to the CHANGELOG file.
