%global pypi_name influxdb

Name:           python-%{pypi_name}
Version:        3.0.0
Release:        2%{?dist}
Summary:        InfluxDB client

License:        MIT
URL:            https://github.com/influxdb/influxdb-python
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-setuptools
BuildRequires:  python2-devel
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%description
InfluxDB Python is a client for interacting with InfluxDB. 

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2-requests
Requires:       python2-dateutil
Requires:       pytz
Requires:       python-six

%description -n python2-%{pypi_name}
InfluxDB Python is a client for interacting with InfluxDB.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-requests
Requires:       python3-dateutil
Requires:       python3-pytz
Requires:       python3-six

%description -n python3-%{pypi_name}
InfluxDB Python is a client for interacting with InfluxDB.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build

%install
%py3_install
%py2_install

%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py*egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py*egg-info

%changelog
* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-2
- Rebuild for Python 3.6

* Wed Oct 05 2016 David Hannequin <david.hannequin@gmail.com> - 3.0.0-1
- Initial package.
