Name: subscription-manager-migration-data
Summary: RHN Classic to RHSM migration data
Group: System Environment/Base
License: CC0
Version: 2.0.51
Release: 1
URL: http://redhat.com
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%if (0%{?rhel} > 7 || 0%{?fedora})
BuildRequires: python3-devel
BuildRequires: python3
%global python_runtime %{__python3}
%else
BuildRequires: python2-devel
%global python_runtime %{__python}
%endif

%description
This package provides certificates for migrating a system from
RHN Classic to RHSM.

%prep
%setup -q

# Run sanity-check.py with Python 3
sed -i -e's,python,%{__python3},' Makefile

%build
make -f Makefile build VERSION=%{version}-%{release} PREFIX=$RPM_BUILD_DIR PYTHON=%{python_runtime}

%install
rm -rf $RPM_BUILD_ROOT
make -f Makefile install VERSION=%{version}-%{release} PREFIX=$RPM_BUILD_ROOT RHEL_VER=%{?rhel} PYTHON=%{python_runtime}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%attr(755,root,root) %dir %{_datadir}/rhsm/product
%attr(755,root,root) %dir %{_datadir}/rhsm/product/RHEL-%{?rhel}
%{_datadir}/rhsm/product/RHEL-%{?rhel}/*pem
%{_datadir}/rhsm/product/RHEL-%{?rhel}/channel-cert-mapping.txt

%changelog
* Fri Dec 13 2019 Christopher Snyder <csnyder@redhat.com> 2.0.51-1
- 1776461: Rebase subscription-manager-migration-data component to the latest
  upstream branch for RHEL 8.2.0 (csnyder@redhat.com)
- 1776461: Update product certs to include those for 8.2 (csnyder@redhat.com)

* Fri Dec 13 2019 Christopher Snyder <csnyder@redhat.com>
- 1776461: Rebase subscription-manager-migration-data component to the latest
  upstream branch for RHEL 8.2.0 (csnyder@redhat.com)
- 1776461: Update product certs to include those for 8.2 (csnyder@redhat.com)

* Thu Jul 11 2019 Christopher Snyder <csnyder@redhat.com> 2.0.49-1
- Bump release for gating tests 

* Fri Jun 28 2019 Christopher Snyder <csnyder@redhat.com> 2.0.48-1
- Version bump for gating tests

* Fri Jun 28 2019 Christopher Snyder <csnyder@redhat.com> 2.0.47-1
- 1709424: Add 8.1 product certs (csnyder@redhat.com)
- Add 8.1 tito releaser (csnyder@redhat.com)

* Thu Mar 07 2019 Christopher Snyder <csnyder@redhat.com> 2.0.46-1
- 1637733: Add RHEL 8 product certs (csnyder@redhat.com)

* Tue Jul 31 2018 Petr Viktorin <pviktori@redhat.com> - 1.15.0-8
- Run sanity-check.py with Python 3
  https://bugzilla.redhat.com/show_bug.cgi?id=1595816
  https://bugzilla.redhat.com/show_bug.cgi?id=1610038

* Mon Mar 26 2018 Christopher Snyder <csnyder@redhat.com> 2.0.41-1
- 1555913: Remove unused certs (6.10) (csnyder@redhat.com)

* Mon Mar 26 2018 Christopher Snyder <csnyder@redhat.com> 2.0.40-1
- 1555913: Include RHEL 6.10 certs (csnyder@redhat.com)

* Mon Feb 26 2018 Christopher Snyder <csnyder@redhat.com> 2.0.39-1
- 1436850: Update migration data license to CC0 (csnyder@redhat.com)

* Mon Feb 26 2018 Christopher Snyder <csnyder@redhat.com> 2.0.38-1
- 1510200: Rebase subscription-manager-migration-data component to the latest
  upstream branch for RHEL 7.5 (csnyder@redhat.com)

* Mon Jun 12 2017 Kevin Howell <khowell@redhat.com> 2.0.37-1
- 1436441: Add SAP ppc64le cert (khowell@redhat.com)

* Mon Jun 05 2017 Kevin Howell <khowell@redhat.com> 2.0.36-1
- 1436441: Update to latest product cert data (khowell@redhat.com)

* Tue Mar 21 2017 Kevin Howell <khowell@redhat.com> 2.0.35-1
- 1427901: Rebase subscription-manager-migration-data component to the latest
  upstream branch for RHEL 7.4 (khowell@redhat.com)
* Tue Feb 14 2017 Vritant Jain <adarshvritant@gmail.com> 2.0.34-1
- 1286842: rhel-x86_64-server-6-rh-gluster-3-samba-debuginfo channel mapping
  (adarshvritant@gmail.com)

* Tue Jan 31 2017 Vritant Jain <adarshvritant@gmail.com> 2.0.33-1
- 1385446: Rebase subscription-manager-migration-data component to the latest
  upstream branch for RHEL 6.9 (adarshvritant@gmail.com)

* Tue Oct 18 2016 Vritant Jain <adarshvritant@gmail.com> 2.0.32-1
- 1385446: Rebase subscription-manager-migration-data component to the latest
  upstream branch for RHEL 6.9 (adarshvritant@gmail.com)
- Added releaser for 6.9 (adarshvritant@gmail.com)

* Fri Aug 26 2016 Vritant Jain <vrjain@redhat.com> 2.0.31-1
- 1366747: channel-cert-mapping.txt does NOT account for RHN base channel rhel-
  ppc64le-server-7 (vrjain@redhat.com)

* Tue Aug 09 2016 Vritant Jain <vrjain@redhat.com> 2.0.30-1
- 1333545, 1328609, 1349533, 1349584, 1264470, 1349538, 1349592, 1354653,
  1354655: more migration data for RHEL7.3 (vrjain@redhat.com)

* Tue Jun 21 2016 Vritant Jain <vrjain@redhat.com> 2.0.29-1
- 1328579: updated the mappings to point to 7.3 instead of 7.3 Beta
  (vrjain@redhat.com)

* Tue Apr 26 2016 Vritant Jain <adarshvritant@gmail.com> 2.0.28-1
- 1328579:  Add migration-data for RHEL 7.3 (adarshvritant@gmail.com)
- Added 7.3 releaser (adarshvritant@gmail.com)

* Mon Mar 21 2016 Christopher Snyder <csnyder@redhat.com> 2.0.27-1
- 1300766, 1300848: Adds RHEL 6.8 Release Product Certs, Adds rhev-mgmt-agent-*
  mappings back in. (csnyder@redhat.com)

* Tue Feb 09 2016 Christopher Snyder <csnyder@redhat.com> 2.0.26-1
- 1300848: Adding additional migration data (csnyder@redhat.com)

* Wed Jan 20 2016 Christopher Snyder <csnyder@redhat.com> 2.0.25-1
- 1299631: Add migration-data for RHEL 6.8 (csnyder@redhat.com)

* Wed Sep 16 2015 Alex Wood <awood@redhat.com> 2.0.24-1
- 1241221: Add additional migration data for RHEL 7.2 (awood@redhat.com)

* Mon Sep 14 2015 Alex Wood <awood@redhat.com> 2.0.23-1
- 1241221: Add migration data for RHEL 7.2 (awood@redhat.com)

* Fri Jun 05 2015 Alex Wood <awood@redhat.com> 2.0.22-1
- 1228387: Add rhel-ppc64-server-6 base channel. (awood@redhat.com)

* Wed May 20 2015 Alex Wood <awood@redhat.com> 2.0.21-1
- 1222712: Product certificates for RHEL 6.7 (awood@redhat.com)

* Thu May 14 2015 Alex Wood <awood@redhat.com> 2.0.20-1
- 1197864: Add product certificates for RHEL 6.7. (awood@redhat.com)

* Mon Mar 02 2015 Alex Wood <awood@redhat.com> 2.0.19-1
- New certificates for upcoming release. (awood@redhat.com)

* Thu Jan 22 2015 Alex Wood <awood@redhat.com> 2.0.18-1
- 1184653, 1184657: Add new certs for Satellite 5.7 and OpenStack 6.0
  (awood@redhat.com)

* Mon Dec 22 2014 Alex Wood <awood@redhat.com> 2.0.17-1
- 825089: Add AUS product certificates. (awood@redhat.com)

* Mon Dec 22 2014 Alex Wood <awood@redhat.com> 2.0.16-1
- 1176260: Add upstream product certificates. (awood@redhat.com)

* Wed Dec 17 2014 Alex Wood <awood@redhat.com> 2.0.15-1
- 1148110: Add product certificates for RHEL 7.1 (awood@redhat.com)

* Mon Nov 17 2014 Alex Wood <awood@redhat.com> 2.0.14-1
- Adding newest product certificates. (awood@redhat.com)

* Thu Sep 04 2014 Alex Wood <awood@redhat.com> 2.0.13-1
- Update to new channel mappings. (awood@redhat.com)

* Thu Aug 21 2014 jesus m. rodriguez <jesusr@redhat.com> 2.0.12-1
- Create new channel mappings based on most recent rcm-metadata.  (jesusr@redhat.com)
- Updating rcm-metadata (jesusr@redhat.com)

* Wed Aug 13 2014 jesus m. rodriguez <jesusr@redhat.com> 2.0.11-1
- Create new channel mappings based on most recent rcm-metadata. (jesusr@redhat.com)
- Updating rcm-metadata (jesusr@redhat.com)

* Wed Jul 16 2014 Alex Wood <awood@redhat.com> 2.0.10-1
- 1105656: Alter mapping for es-4-els (awood@redhat.com)

* Wed Jul 16 2014 Alex Wood <awood@redhat.com> 2.0.9-1
- Create new channel mappings based on most recent rcm-metadata.
  (awood@redhat.com)

* Wed May 07 2014 ckozak <ckozak@redhat.com> 2.0.8-1
- Updated releasers for rhel5.11 (ckozak@redhat.com)
- Add mappings for RHEL 5.11 (awood@redhat.com)

* Tue Feb 18 2014 ckozak <ckozak@redhat.com> 2.0.7-1
- Invoke sanity-check.py with python and require python for build.
  (awood@redhat.com)

* Tue Feb 18 2014 ckozak <ckozak@redhat.com> 2.0.6-1
- Add RHEL 7 certs. (awood@redhat.com)

* Thu Oct 17 2013 Alex Wood <awood@redhat.com> 2.0.5-1
- 1009932: Add RHEL 4 mappings to migration data. (awood@redhat.com)

* Thu Sep 26 2013 Alex Wood <awood@redhat.com> 2.0.4-1
- Adding RHEL 6.5 certificates. (awood@redhat.com)
- Detect invalid channels more generally. (awood@redhat.com)

* Wed Sep 25 2013 Alex Wood <awood@redhat.com> 2.0.3-1
- 1011992: Skip high touch beta channels. (awood@redhat.com)

* Wed Sep 11 2013 Alex Wood <awood@redhat.com> 2.0.2-1
- Updating product cert mappings. (awood@redhat.com)
- Point to newest rcm-metadata (awood@redhat.com)
- Adding file explaining how to build on Fedora. (awood@redhat.com)

* Thu Jun 06 2013 Alex Wood <awood@redhat.com> 2.0.1-1
- new package built with tito

* Wed Jun 05 2013 Alex Wood <awood@redhat.com> 2.0.0-1
- Unifying all RHEL product certificates into one package

* Thu May 09 2013 Alex Wood <awood@redhat.com> 1.11.3.0-1
- Adding product certificates for RHEL 5.10

* Fri Oct 12 2012 Alex Wood <awood@redhat.com> 1.11.2.7-1
- 865566: Add mappings for RHEV debuginfo channels. (awood@redhat.com)

* Tue Oct 02 2012 Alex Wood <awood@redhat.com> 1.11.2.6-1
- Removing unused product certificate. (awood@redhat.com)

* Tue Oct 02 2012 Alex Wood <awood@redhat.com> 1.11.2.5-1
- 861420: Add mapping and certificates for RHEV 3.0. (awood@redhat.com)
- 861470: Add mapping and certificates for ELS-JBEAP. (awood@redhat.com)

* Wed Aug 29 2012 Alex Wood <awood@redhat.com> 1.11.2.4-1
- Adding product certificate for RHB i386. (awood@redhat.com)
- 820749: Correct mappings for i386 DTS. (awood@redhat.com)
- 849274, 849305: Update mappings for JBEAP and RHEV Agent. (awood@redhat.com)

* Thu Aug 09 2012 Alex Wood <awood@redhat.com> 1.11.2.3-1
- Correcting logic on special hack for 180.pem (awood@redhat.com)
- Adding additional product certs and mappings. (awood@redhat.com)
- Adding special hack for 17{6|8}.pem and 180.pem (awood@redhat.com)
- 840148: Adding cert and mapping for Server-EUCJP (awood@redhat.com)

* Thu Jun 28 2012 Alex Wood <awood@redhat.com> 1.11.2.2-1
- Product mappings for RHEL5.9 (awood@redhat.com)

* Tue Jan 17 2012 Alex Wood <awood@redhat.com> 1.11-1
- 782208: Use RHEL 5.8 certificates. (awood@redhat.com)

* Mon Jan 09 2012 Alex Wood <awood@redhat.com> 1.10-1
- 771615: Remove a dependency on the Linux 'file' command from the linting
  script. (awood@redhat.com)

* Mon Jan 09 2012 Alex Wood <awood@redhat.com> 1.9-1
- Remove a dependency on the Linux 'file' command from the linting script.
  (awood@redhat.com)

* Mon Jan 09 2012 Alex Wood <awood@redhat.com> 1.8-1
- 771615: fix mapping file syntax errors (jbowes@redhat.com)
- 771615: add sanity-check script for mappings (jbowes@redhat.com)
- update gitignore for swap files (jbowes@redhat.com)

* Thu Dec 15 2011 Alex Wood <awood@redhat.com> 1.7-1
- 767749: subscription-manager-migration-data should require subscription-
  manager-migration. (awood@redhat.com)

* Mon Nov 28 2011 Alex Wood <awood@redhat.com> 1.6-1
- 757829: Fixing license field. (awood@redhat.com)

* Mon Nov 28 2011 Alex Wood <awood@redhat.com> 1.5-1
- Changing text of license field. (awood@redhat.com)

* Mon Nov 21 2011 Alex Wood <awood@redhat.com> 1.4-1
- Adding CVS releaser. (awood@redhat.com)

* Mon Nov 21 2011 Alex Wood <awood@redhat.com> 1.3-1
- 755035: Genericize to RHEL-5 instead of just RHEL-5.7 (awood@redhat.com)

* Thu Nov 17 2011 Alex Wood <awood@redhat.com> 1.2-1
- Correcting incorrect date in the changelog. (awood@redhat.com)
- alter license per mkhusid (he is following up w/ legal to confirm)
  (cduryee@redhat.com)
- rpmlint fixes (cduryee@redhat.com)
- Removing .svn directory that was checked in accidentally. (awood@redhat.com)

* Wed Nov 02 2011 Alex Wood <awood@redhat.com> 1.1-1
- new package built with tito

* Tue Nov 01 2011 Alex Wood <awood@redhat.com> 1.0.0-1
- Initial packaging.

