%define		_state		stable
%define		orgname		kreversi
%define		qtver		4.8.0

Summary:	KDE Reversi game
Summary(pl.UTF-8):	Gra Reversi dla KDE
Summary(pt_BR.UTF-8):	Jogo no estilo Otelo para KDE
Name:		kde4-%{orgname}
Version:	4.14.3
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	2f7f3d9666557787b170fcd97e06e6db
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reversi is a simple strategy game that is played by two players. There
is only one type of piece - one side of it is black, the other white.
If a player captures a piece on the board, that piece is turned and
belongs to that player. The winner is the person that has more pieces
of his own color on the board and if there are no more moves possible.

%description -l pl.UTF-8
Reversi to prosta gra strategiczna dla dwóch graczy. Jest tylko jeden
rodzaj pionu - z jednej strony czarny, z drugiej biały. Jeśli gracz
schwyta pion na planszy, jest on obracany i należy do tego gracza.
Zwycięzcą jest osoba, która ma na planszy więcej pionów w swoim
kolorze w chwili, gdy nie można już wykonać żadnego ruchu.

%description -l pt_BR.UTF-8
Jogo no estilo Otelo para KDE.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kreversi
%{_desktopdir}/kde4/kreversi.desktop
%{_datadir}/apps/kreversi
%{_iconsdir}/*/*/actions/legalmoves.png
%{_iconsdir}/*/*/actions/lastmoves.png
%{_iconsdir}/*/*/apps/kreversi.png
%{_iconsdir}/oxygen/scalable/actions/*.svgz
