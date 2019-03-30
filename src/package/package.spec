# -*- mode: python -*-

block_cipher = None

a = Analysis(['../nlp/__init__.py'],
             pathex=['C:\\Projects\\nlu'],
             binaries=[('scipy/extra-dll', '.')],
             datas=[],
             hiddenimports=['tensorflow.contrib','_corecffi','gevent','gevent.__hub_local','gevent._queue','gevent._local', 'gevent.__semaphore','gevent.time','sqlalchemy','actions','jpype','dateutil', 'six', 'flask','scipy', 'scipy._lib.messagestream', 'sklearn', 'sklearn.neighbors.typedefs', 'spacy', 'tensorflow', 'cymem.cymem', 'thinc.linalg', 'murmurhash.mrmr', 'cytoolz.utils', 'cytoolz._signatures', 'spacy.strings', 'spacy.morphology', 'spacy.lexeme', 'spacy.tokens.underscore', 'spacy.tokens', 'spacy.gold', 'spacy.parts_of_speech', 'dill', 'spacy.tokens.printers', 'spacy.tokens._retokenize', 'spacy.syntax', 'spacy.syntax.stateclass', 'spacy.syntax.transition_system', 'spacy.syntax.nonproj', 'spacy.syntax.nn_parser', 'spacy.syntax.arc_eager', 'thinc.extra.search', 'spacy.syntax._beam_utils', 'spacy.syntax.ner', 'thinc.neural._classes.difference', 'spacy.lang', 'spacy.lang.en','gevent', 'gevent.__hub_local', 'gevent.__greenlet_primitives', 'gevent.__waiter','gevent.__hub_primitives', 'gevent.get_hub', 'gevent.libev', 'gevent.libev.corecffi', 'event.libev._corecffi', 'gevent.builtins', 'gevent.socket', 'gevent._event', 'gevent.__ident', 'gevent._greenlet', 'gevent.threading', 'gevent.thread', 'gevent.ssl', 'pycrfsuite._pycrfsuite', 'pycrfsuite._dumpparser', 'pycrfsuite._logparser', 'numpy.core._dtype_ctypes', '_ufuncs','scipy.integrate', 'scipy.integrate.quadpack', 'scipy.integrate._vode', 'scipy.special._ufuncs', 'tornado'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='nlp',
          debug=True,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='nlp')
