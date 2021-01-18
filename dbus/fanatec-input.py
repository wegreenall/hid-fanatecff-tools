#!/usr/bin/python

from pydbus.generic import signal
import glob
  
FANATEC_VENDOR_ID='0EB7'
CSL_ELITE_PEDALS_DEVICE_ID='6204'
CSL_ELITE_PS4_WHEELBASE_DEVICE_ID='0005'

def get_sysfs_base(PID):
  return glob.glob("/sys/module/hid_fanatec/drivers/hid:ftec_csl_elite/0003:%s:%s.*"%(FANATEC_VENDOR_ID, PID))[0]

class CSLElite(object):
  """
    <node>
      <interface name='org.fanatec.CSLElite'>
        <property name="SLOT" type="i" access="readwrite">
          <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
        </property>
        <property name="SEN" type="i" access="readwrite">
          <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
        </property>
        <property name="FF" type="i" access="readwrite">
          <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
        </property>
        <property name="DRI" type="i" access="readwrite">
          <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
        </property>
        <property name="FEI" type="i" access="readwrite">
          <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
        </property>
        <property name="FOR" type="i" access="readwrite">
          <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
        </property>
        <property name="SPR" type="i" access="readwrite">
          <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
        </property>
        <property name="DPR" type="i" access="readwrite">
          <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
        </property>            
        <property name="BLI" type="i" access="readwrite">
          <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
        </property>      
        <property name="SHO" type="i" access="readwrite">
          <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
        </property>                                                                  
      </interface>    
    </node>
  """
  def __init__(self):
    pass

  def get_sysfs(self, name):
    return "%s/%s"%(get_sysfs_base(CSL_ELITE_PS4_WHEELBASE_DEVICE_ID), name)

  def tuning_get(self, name):
    return int(open(self.get_sysfs(name),'r').read())

  def tuning_set(self, name, value):
    return int(open(self.get_sysfs(name),'w').write(str(value)))

  @property
  def SLOT(self):
    return self.tuning_get('SLOT')

  @SLOT.setter
  def SLOT(self, value):
    return self.tuning_set('SLOT', value)

  @property
  def SEN(self):
    return self.tuning_get('SEN')

  @SEN.setter
  def SEN(self, value):
    return self.tuning_set('SEN', value)

  @property
  def FF(self):
    return self.tuning_get('FF')

  @FF.setter
  def FF(self, value):
    return self.tuning_set('FF', value)

  @property
  def DRI(self):
    return self.tuning_get('DRI')

  @DRI.setter
  def DRI(self, value):
    return self.tuning_set('DRI', value)

  @property
  def FEI(self):
    return self.tuning_get('FEI')

  @FEI.setter
  def FEI(self, value):
    return self.tuning_set('FEI', value)

  @property
  def FOR(self):
    return self.tuning_get('FOR')

  @FOR.setter
  def FOR(self, value):
    return self.tuning_set('FOR', value)

  @property
  def SPR(self):
    return self.tuning_get('SPR')

  @SPR.setter
  def SPR(self, value):
    return self.tuning_set('SPR', value)

  @property
  def DPR(self):
    return self.tuning_get('DPR')

  @DPR.setter
  def DPR(self, value):
    return self.tuning_set('DPR', value)

  @property
  def BLI(self):
    return self.tuning_get('BLI')

  @BLI.setter
  def BLI(self, value):
    return self.tuning_set('BLI', value)
  
  @property
  def SHO(self):
    return self.tuning_get('SHO')

  @SHO.setter
  def SHO(self, value):
    return self.tuning_set('SHO', value)


class CSLElitePedals(object):
  """
    <node>
      <interface name='org.fanatec.CSLElite.Pedals'>
        <property name="Load" type="i" access="readwrite">
          <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
        </property>
      </interface>
    </node>
  """

  def __init__(self):
    pass
  
  def get_sysfs(self, name):
    return "%s/%s"%(get_sysfs_base(CSL_ELITE_PEDALS_DEVICE_ID), name)

  @property
  def Load(self):
    return int(open(self.get_sysfs('load'),'r').read())

  @Load.setter
  def Load(self, value):
    return int(open(self.get_sysfs('load'),'w').write(str(value)))

  PropertiesChanged = signal()


class CSLEliteWheel(object):
  """
    <node>
      <interface name='org.fanatec.CSLElite.Wheel'>
        <property name="Display" type="i" access="write">
          <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
        </property>
        <property name="RPM" type="ab" access="write">
          <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
        </property>        
      </interface>
    </node>
  """

  def __init__(self):
    pass

  def get_sysfs(self, name):
    return "%s/%s"%(get_sysfs_base(CSL_ELITE_PS4_WHEELBASE_DEVICE_ID), name)
  
  def get_sysfs_rpm(self):
    sysfs_base = get_sysfs_base(CSL_ELITE_PS4_WHEELBASE_DEVICE_ID)
    return "%s/leds/0003:0EB7:%s.%s::RPM"%(sysfs_base,CSL_ELITE_PS4_WHEELBASE_DEVICE_ID,sysfs_base.split(".")[-1])
  
  @property
  def Display(self):
    return 0

  @property
  def RPM(self):
    return 0

  @Display.setter
  def Display(self, value):
    return int(open(self.get_sysfs('display'),'w').write(str(value)))

  @RPM.setter
  def RPM(self, values):
    return list(map(lambda i: open('%s%i/brightness'%(self.get_sysfs_rpm(), i[0] + 1),'w').write('1' if i[1] else '0'), enumerate(values)))

  PropertiesChanged = signal()


if __name__ == "__main__":
  from pydbus import SystemBus
  from gi.repository import GLib

  bus = SystemBus()
  r = bus.publish('org.fanatec.CSLElite', CSLElite(),
    ('Pedals', CSLElitePedals()),
    ('Wheel', CSLEliteWheel()))
  try:
      loop = GLib.MainLoop()
      loop.run()
  except (KeyboardInterrupt, SystemExit):
      print("Exiting")
  except Exception as e:
      raise e        
  finally:
      r.unpublish()
