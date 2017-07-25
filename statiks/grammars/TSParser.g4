grammar TSParser;

CUR: 'EUR' | 'USD';
fragment CURSIGN: '\u20AC' | '$';
fragment CENTS: [0-9][0-9];
fragment INT     : [0-9]+ ;
fragment DATE:  INT'/'INT'/'INT;
fragment TIME: INT':'INT':'INT ' ' ('CET'|'ET');
PLAYERS: INT ' players';
MONEY: CURSIGN INT '.' CENTS;
GAME: 'No Limit Hold\'em';
TID: ('T' | '#') INT;
PERCENTAGE: INT '%';
TOURNSTARTED: 'Tournament started ';
PERSONAL: 'You finished in ' WORD ' place (eliminated at hand ' TID ').';
DATETIME: TOURNSTARTED DATE ' ' TIME ' [' DATE ' ' TIME ']' NEWLINE;
NEWLINE : [\r\n]+;
PLACESUFFIX: [0-9]?[0-9]?[0-9]?[0-9]?[0-9]?[0-9][a-z][a-z];
WORDS: WORD ((' ')? WORD)*;
fragment WORD: [a-zA-Z0-9]+;

ts: description buyin players prizepool DATETIME results PERSONAL;
description: 'PokerStars Tournament ' TID ', ' GAME NEWLINE;
buyin: 'Buy-In: ' cost=buyincost NEWLINE;
buyincost: MONEY '/' MONEY ' ' CUR;
players: PLAYERS NEWLINE;
prizepool: 'Total Prize Pool: ' MONEY ' ' CUR NEWLINE;
results: playerlist;
playerlist: player playerlist | player;
player: '  ' WORDS ': ' WORDS ' (' WORDS '),' ((prize)?|' still playing') NEWLINE;
prize: MONEY '(' PERCENTAGE ')';

