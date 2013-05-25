from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty, AliasProperty, StringProperty, DictProperty, BooleanProperty, StringProperty, OptionProperty
from boardwidgets import Stone, TextMarker, TriangleMarker, SquareMarker, CircleMarker, CrossMarker, VarStone

class WidgetCache(object):
    # Cached board widgets
    blackstonecache = []
    whitestonecache = []
    labelcache = {}
    varstonecache = []
    shapecache = {}
    def get_black_stone(self,size=(0,0),pos=(0,0)):
        bsc = self.blackstonecache
        if len(bsc) > 0:
            stone = bsc.pop(0)
        else:
            stone = Stone()
            stone.set_colour('black')
        return stone
    def cache_black_stone(self,stone):
        self.blackstonecache.append(stone)
    def get_white_stone(self,size=(0,0),pos=(0,0)):
        wsc = self.whitestonecache
        if len(wsc) > 0:
            stone = wsc.pop(0)
        else:
            stone = Stone()
            stone.set_colour('white')
        return stone
    def cache_white_stone(self,stone):
        self.whitestonecache.append(stone)
    def get_stone(self,colour='b'):
        if colour == 'b':
            return self.get_black_stone()
        elif colour == 'w':
            return self.get_white_stone()
        else:
            print 'asked for stone colour that doesn\'t exist'
    def cache_stone(self,stone,colour):
        if colour == 'b':
            self.cache_black_stone(stone)
        elif colour == 'w':
            self.cache_white_stone(stone)
        else:
            print 'asked to cache stone colour that doesn\'t exist'
    def get_label(self,text):
        lc = self.labelcache
        if lc.has_key(text):
            labels = lc[text]
            label = labels.pop(0)
            print 'got',label,'from',labels
            if len(labels) == 0:
                lc.pop(text)
            return label
        if len(lc) > 0:
            alttext = lc.keys()[0]
            labels = lc[alttext]
            label = labels.pop(0)
            if len(labels)==0:
                lc.pop(alttext)
            label.text = text
            return label
        label = TextMarker(text=text)
        return label
    def cache_label(self,label):
        text = label.text
        lc = self.labelcache
        if not lc.has_key(text):
            lc[text] = []
        lc[text].append(label)
    def get_var_stone(self):
        vsc = self.varstonecache
        if len(vsc)>0:
            varstone = vsc.pop(0)
        else:
            varstone = VarStone()
        return varstone
    def cache_var_stone(self,varstone):
        self.varstonecache.append(varstone)
    def get_shape_marker(self, shape):
        sc = self.shapecache
        print 'asked for shape marker',shape,sc
        if sc.has_key(shape):
            markers = sc[shape]
            marker = markers.pop(0)
            if len(markers) == 0:
                sc.pop(shape)
            return marker
            
        if shape == 'triangle':
            return TriangleMarker()
        elif shape == 'square':
            return SquareMarker()
        elif shape == 'circle':
            return CircleMarker()
        elif shape == 'cross':
            return CrossMarker()
    def cache_shape_marker(self,marker):
        sc = self.shapecache
        print 'asked to cache shape marker',marker,sc
        if isinstance(marker,TriangleMarker):
            try:
                sc['triangle'].append(marker)
            except KeyError:
                sc['triangle'] = [marker]
        elif isinstance(marker,SquareMarker):
            try:
                sc['square'].append(marker)
            except KeyError:
                sc['square'] = [marker]
        elif isinstance(marker,CrossMarker):
            try:
                sc['cross'].append(marker)
            except KeyError:
                sc['cross'] = [marker]
        elif isinstance(marker,CircleMarker):
            try:
                sc['circle'].append(marker)
            except KeyError:
                sc['circle'] = [marker]
    def cache_marker(self,marker):
        if isinstance(marker,TextMarker):
            self.cache_label(marker)
        else:
            self.cache_shape_marker(marker)
    