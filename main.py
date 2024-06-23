
######
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen,ScreenManager,FadeTransition



from webbrowser import open as op

from kivy.uix.textinput import TextInput
from android.permissions import Permission,request_permissions,check_permission,request_permission




from plyer import notification,vibrator

import kivmob

from kivy.uix.popup import Popup

from kivy.core.window import Window

from kivy.clock import Clock

from kivy.uix.rst import RstDocument



#######
from os import popen
from os.path import exists
di='/storage/emulated/0'


def h(t):
	global di
	g=t.split()
	
	if 'cd' in g:
		jk=g[g.index('cd')+1:]
		
		if ''.join(jk)=='..':
			hh=di.split('/')[:-1]
			hd=''
			for i in hh:
				hd+=i+'/'
			di=hd
		
		elif exists(di+'/'+''.join(jk)):
			if di.endswith('0'):
				di=di+'/'+''.join(jk)
			
			elif di.endswith('/'):
				
				di=di+''.join(jk)
				
			else:
				di=di+'/'+''.join(jk)
		
			
		elif exists(''.join(jk)):
			di=''.join(jk)
		return True
		


def syso(t):
	
	if not h(t):
	
		ghk=popen(f'cd {di} ; {t}').read()
		return ghk
	
	


#####

kv="""
Home:
	Sc:
	Sc1:
	Sc2:
		
<Sc>:
	name:'screen'
	BoxLayout:
		orientation:'vertical'
		BoxLayout:
			id:drx
			size_hint_y:None
			height:150
			Button:
				text:'bash'
				color:0,1,0,1
				background_color:0,0,1,1
				on_press:
					app.root.current='screen2'
					app.tes()
				
			Button:
				text:'files'
				color:0,1,0,1
				background_color:0,0,1,1
				on_press:
					app.root.current='screen1'
			
		ScrollView:
			BoxLayout:
				
				orientation:'vertical'
				size_hint_y:None
				height:self.minimum_height
				
				Label:
					size_hint_y:None
					text:''
				Button:
					size_hint_y:None
					background_color:1,0,0,1
					color:0,1,0,1
					height:150
					text:'Telegram Channel'
					on_press:
						app.ops()
				Label:
					size_hint_y:None
					height:50
					
				Button:
					size_hint_y:None
					background_color:1,0,0,1
					color:0,1,0,1
					heght:150
					text:'About'
					on_press:
						root.popabout()
				Label:
					size_hint_y:None
					height:75
				Button:
					size_hint_y:None
					background_color:1,0,0,1
					color:0,1,0,1
					heght:150
					text:'show toast'
					on_release:
						app.toast()
				Label:
					size_hint_y:None
					height:35
				Button:
					size_hint_y:None
					background_color:1,0,0,1
					color:0,1,0,1
					heght:150
					text:'show notification'
					on_release:
						app.notify()
				Label:
					size_hint_y:None
					height:35
				Button:
					size_hint_y:None
					background_color:1,0,0,1
					color:0,1,0,1
					heght:150
					text:'ran vibrate'
					on_release:
						app.vibrate()
				Label:
					size_hint_y:None
					height:35
				Button:
					size_hint_y:None
					background_color:1,0,0,1
					color:0,1,0,1
					heght:150
					text:'banner ads'
					on_release:
						app.ads()
				
				
			



		Label:
			size_hint_y:None
			text:'© Ali'
			color:0,1,0,1
		
<Sc1>:
	name:'screen1'
	BoxLayout:
		id:sid
		orientation:'vertical'
		
		FileChooserIconView:
            show_hidden: True
            path:'/storage/emulated/0'
        Button:
			size_hint_y:None
			text:'back'
			background_color:1,0,0,1
			color:0,1,0,1
			on_press:
				app.root.current='screen'
			

<Sc2>:
	name:'screen2'
	BoxLayout:
		orientation:'vertical'
		BoxLayout:
			size_hint_y:None
			height:150
			Button:
				text:'back'
				color:1,0,0,1
				background_color:0,1,0,1
				on_press:
					app.root.current='screen'
				
			Label:
			Button:
				text:'run'
				color:1,0,0,1
				background_color:0,1,0,1
				on_press:root.reso()
			Label:
			Button:
				text:'clear'
				color:1,0,0,1
				background_color:0,1,0,1
				on_press:root.cles()
		BoxLayout:
			id:sudo
			orientation:'vertical'
			Label:
				id:lab
				size_hint_y:None
					
				text:root.url
				font_size:50
				color:0,0,1,1
				
			BoxLayout:
				size_hint_y:None
				Label:
					
					size_hint_x:None
					
					text:'_$'
					font_size:50
					color:0,0,1,1
					background_color:0,1,0,1
					
				TextInput:
					id:htext
					font_size:50
					#text:'_$'
					size_hint_y:None
					background_color:0,1,0,1#'000000'
				
					cursor_color:1,0,0,1
					cursor_width:25
					cursor_blink:False
					multiline:False
					foreground_color:0,0,1,1
					on_text_validate:
						root.reso()
				
				
				
			BoxLayout:
				ScrollView:
					BoxLayout:
						orientation:'vertical'
						height:self.minimum_height
						id:redo
						RstDocument:




"""


TextInput.on_text_validate

class Home(ScreenManager):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.transition=FadeTransition()


	
	
class Sc(Screen):
	we,he=Window.size
	
	def popabout(self):
		
		gh=Popup(title='About',size_hint=(None,None),size=(self.we-100,600))
		g=BoxLayout(orientation='vertical')
		g.add_widget(Label(text='this is test app'))
		
		bb=Button(size_hint=(None,None),text='close',width=150,color=(1,0,0,1),background_color=(0,1,0,1))
		bb.bind(on_press=lambda self:gh.dismiss())
		g.add_widget(bb)
		
		#self.gh=Popup(title='About',content=g,size_hint=(None,None),size=(self.we-100,600))
		gh.content=g
		gh.open()
	
		
		
		
		
class Sc1(Screen):
	pass

class Sc2(Screen):
	def cles(self):
		self.ids.redo.clear_widgets()
		self.ids.redo.add_widget(RstDocument(text=''))
		
	
	global di
	url=di
	def urls(self):
		self.ids.lab.text=di
	def reso(self):
			g=syso(self.ids.htext.text)
			h=self.ids.redo
			h.clear_widgets()
		
			t=RstDocument(text=g)
			h.add_widget(t)
			
			if 'cd' in self.ids.htext.text.split():
				self.urls()
			self.ids.htext.text=''
		



class Mad(App):
	def tes(self):
		
		Sc2().ids.htext.focus=True
		
	
	clear=lambda self ,x:Clock.schedule_interval(self.cle(x),0.1)
	def cle(self, si):
	    for i in si.children[:]:
	    	si.remove_widget(i)
	
	def ops(self):
		op('https://t.me/p5_0k')
	
	def ads(self):
		try:
			ad=kivmob.KivMob(kivmob.TestIds.APP)
			ad.new_banner(kivmob.TestIds.BANNER,top_pos=True)
			ad.request_banner()
			ad.show_banner()
		except:
			pass
	
	def vibrate(self):
		vibrator.vibrate(1)
	
	def notify(self):
		notification.notify(title='this is title',message='this is message')
	
	def toast(self):
		try:
			notification.notify(toast=True,message='this is a toast')
		except:
			pass
	
	
	def build(self):
		try:
			request_permissions([Permission.WRITE_EXTERNAL_STORAGE,Permission.READ_EXTERNAL_STORAGE,Permission.VIBRATE])
		except:
			pass
		
		
		
		
		return Builder.load_string(kv)


Mad().run()


