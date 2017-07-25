grammar TournamentSummary;

CURSIGN: '\u20AC' | '$';
CUR: 'EUR' | 'USD';
CENTS: [0-9][0-9];
INT     : [0-9]+ ;
WORDS: [a-zA-Z0-9]+((' ')? [a-zA-Z0-9]+)*;
NEWLINE : [\r\n]+;
TSNAME: 'TS' INT;
TID: ('T' | '#') INT;
PLACESUFFIX: [0-9]?[0-9]?[0-9]?[0-9]?[0-9]?[0-9][a-z][a-z];
GAME: 'No Limit Hold\'em';

ts: description buyin players prizepool datetime results personal;
//title: TSNAME TID GAME BUYIN;
description: 'PokerStars Tournament ' TID ', ' GAME NEWLINE;
buyin: 'Buy-In: ' buyincost ' ' CUR NEWLINE;
buyincost: money '/' money ' ' CUR;
money: CURSIGN INT '.' CENTS;
players: INT ' players' NEWLINE;
prizepool: 'Total Prize Pool: ' money CUR NEWLINE;
datetime: 'Tournament started ' date ' ' time ' [' date ' ' time ']' NEWLINE;
date:  INT'/'INT'/'INT;
time: INT':'INT':'INT ' ' ('CET'|'ET');
results: NEWLINE playerlist NEWLINE;
playerlist: '  ' player playerlist | player;
player: INT ': ' WORDS ' (' WORDS '),' ((prize)?|' still playing') NEWLINE;
prize: money '(' percentage ')';
personal: 'You finished in ' place ' place (eliminated at hand ' TID ').';
place: PLACESUFFIX;
percentage: INT '%';

